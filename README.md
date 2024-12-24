# 🔎 Query Mind  

**A Streamlit-powered chatbot capable of performing web searches and retrieving information from Arxiv, Wikipedia, and DuckDuckGo!**  

---

## 🌟 Features  

- **🔍 Multi-Source Querying**: Search for information across Arxiv, Wikipedia, and the web (via DuckDuckGo).  
- **🧠 Intelligent Chatbot**: Powered by ChatGroq with the advanced Llama3-8b-8192 model for accurate and contextual responses.  
- **📑 Streamlined Results**: Retrieves concise and meaningful data with customizable search settings.  
- **🎨 Interactive UI**: User-friendly interface designed with Streamlit.  
- **🔒 Secure API Key Input**: Easily input and manage your Groq API Key via the sidebar.  

---

## 🛠️ Tech Stack  

- **Programming Language**: Python 🐍  
- **Web Framework**: Streamlit 🌟  
- **Language Models**: ChatGroq 🤖  
- **Tools**:  
  - ArxivAPIWrapper 📚  
  - WikipediaAPIWrapper 🌐  
  - DuckDuckGoSearchRun 🦆  
- **Environment Management**: Python dotenv 🔑  

---

## 📋 Prerequisites  

Make sure the following are installed:  

- Python 3.8+ 🐍  
- Streamlit  
- LangChain  
- dotenv  

---

## 🚀 Quick Start  

1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/YourUsername/QueryMind.git  
   ```  

2. **Navigate to the project directory**:  
   ```bash  
   cd QueryMind  
   ```  

3. **Install dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. **Set up environment variables**:  
   Create a `.env` file in the root directory:  
   ```  
   GROQ_API_KEY=your_groq_api_key  
   ```  

5. **Run the application**:  
   ```bash  
   streamlit run app.py  
   ```  

6. **Access the app**:  
   Open your browser and go to: `http://localhost:8501` 🌐  

---

## 🔧 How It Works  

1. **Input Queries**: Type a question or prompt in the input box.  
2. **Search Sources**:  
   - 🦆 DuckDuckGo for general web search.  
   - 📚 Arxiv for academic research.  
   - 🌐 Wikipedia for encyclopedic information.  
3. **Receive Answers**: Get concise, relevant results displayed in a conversational format.  

---

## 🛡️ Security  

- API keys are managed securely via `.env` files.  
- Sensitive information like the Groq API key is entered through the sidebar for added security.  

---

## 🤝 Contributions  

Contributions are welcome! Feel free to:  

- Open issues 🐛  
- Submit pull requests 🚀  
- Share feedback 💡  

---  

Enjoy using **🔎 Query Mind** for all your information retrieval needs! 🎉  

---  

Let me know if you'd like any changes or additions!
