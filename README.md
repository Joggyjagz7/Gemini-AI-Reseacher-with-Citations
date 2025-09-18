# 🤖 AI Content Generator with In-Text Citations (RAG)

This project is a web-based application that demonstrates a powerful **Retrieval-Augmented Generation (RAG)** system. It allows users to upload their own source documents (like reports, articles, or notes) and generate new content based on a prompt.

Crucially, every piece of generated information is traceable, with **in-text citations** linking back to the original source material. This prevents the AI from using external knowledge and ensures factual accuracy relative to the provided sources.

---

## ✨ Key Features

* **Bring Your Own Data**: Upload multiple local text files (`.txt`, `.md`) to create a custom knowledge base for each session.
* **Context-Aware Generation**: The AI's response is strictly limited to the information contained within your uploaded documents.
* **Automatic In-Text Citations**: The generated content includes citation markers (e.g., `[Source 1]`) directly in the text.
* **Verifiable Sources**: A "Sources Used" section is generated, showing which documents and text snippets were used to create the answer.
* **Modern Web Interface**: A clean, user-friendly interface built with Tailwind CSS.
* **Fast & Efficient**: Powered by Google's `gemini-2.5-flash-preview-05-20` model for quick responses.
* **Self-Contained & Local**: Can be easily run on your local machine using a simple Python Flask server.

---

## ⚙️ How It Works: The RAG Pipeline

This application performs the entire RAG process in the user's browser and through an API call, without needing a complex backend or database.

1.  **Loading & Chunking (Client-Side)**: When you upload files, the JavaScript in your browser reads the text and splits it into smaller, manageable "chunks" (in this case, by paragraphs).
2.  **Retrieval (Client-Side)**: When you write a prompt and click "Generate," the application performs a simple keyword-based search to find the most relevant chunks from your documents. This is the **Retrieval** step.
3.  **Augmentation**: The user's original prompt and the content of the top-ranked chunks are combined into a single, detailed prompt. This "augmented" prompt instructs the AI on its task, provides the necessary context, and tells it to add citations.
4.  **Generation**: This final, augmented prompt is sent to the Google Gemini API. The Large Language Model (LLM) then **Generates** the text based *only* on the context it was given, fulfilling the user's request and embedding the citation markers.
5.  **Display**: The application receives the generated text from the API and displays it, highlighting the citations and listing the corresponding sources.

---

## 🛠️ Technology Stack

* **Frontend**: HTML, Tailwind CSS, Vanilla JavaScript
* **AI Model**: Google Gemini API (`gemini-2.5-flash-preview-05-20`)
* **Local Server Frame**: Python 3, Flask

---

## 🚀 How to Run Locally

Follow these steps to get the application running on your own computer.

### Prerequisites

* Python 3.6 or newer installed on your system.

### Step 1: Set Up Project Files

1.  Create a main project folder named `rag-citation-app`.
2.  Inside it, create the exact folder structure and files as shown below.

    ```
    Gemini-AI-Researcher-app/
    │
    ├── server.py
    └──main-index.html
    ```

### Step 2: Install Dependencies in a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

1.  Open your terminal or command prompt and navigate into the `rag-citation-app` directory.
    ```bash
    cd gemini-ai-researcher-with-citations
    ```
2.  Create and activate the virtual environment:

    * **On macOS / Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * **On Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
3.  Install the required package using pip:
    ```bash
    pip install -r requirements.txt
    ```

### Step 3: Run the Web Server

1.  With your virtual environment still active, run the Flask server:
    ```bash
    python web-server.py
    ```
2.  The terminal will show that the server is running and provide a local URL.
    ```
    Starting the RAG Citation App server...
    Open your browser and navigate to [http://127.0.0.1:5001](http://127.0.0.1:5001)
     * Running on [http://127.0.0.1:5001](http://127.0.0.1:5001)
    ```

### Step 4: Use the Application

1.  Open your web browser (e.g., Chrome, Firefox).
2.  Navigate to the address: **http://127.0.0.1:5001**

You can now use the AI Content Generator on your local machine!

---

## 💡 Future Improvements

This project serves as a great foundation. Here are some ways it could be enhanced:

* **Advanced Retrieval**: Implement vector-based similarity search (e.g., using `sentence-transformers.js`) for more accurate context retrieval.
* **Support More File Types**: Add support for uploading `.pdf` and `.docx` files by integrating client-side parsing libraries.
* **Streaming Responses**: Show the AI's response as it's being generated in real-time.
* **Export Results**: Add a button to download the generated content and sources as a text or markdown file.
