import streamlit as st
from langchain_community.tools import DuckDuckGoSearchRun
import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain.agents import initialize_agent,AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os

arxiv_wrapper=ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)

search = DuckDuckGoSearchRun(name="Search")

st.title("🔎QUERY MIND")

st.sidebar.title("Settings")
api_key = st.sidebar.text_input("enter your groq api key: ", type = "password")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {'role':"assistant","content":"Hello! I am Query Mind, your personal assistant. How can I help you today?"}
    ]
    
for msg in st.session_state.messages:
    st.chat_message(msg["role"].write(msg["content"]))
    
if prompt:=st.chat_input(placeholder='what is machine learning'):
    st.session_state.messages.append({'role':"user","content":prompt})
    st.chat_messgae("user").write(prompt)
    
    llm = ChatGroq(groq_api_key = api_key, model_name = "Llama-8b-8192",streaming=True)
    tools = [arxiv,wiki]
    
    search_agent = initialize_agent(tools, llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION)
    
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(),expand_new_thougts = False)
        response = search_agent.run(st.session_state.messages, callbacks = [st_cb])
        st.session_state.messages.append({'role':"assistant","content":response})
        st.write(response)