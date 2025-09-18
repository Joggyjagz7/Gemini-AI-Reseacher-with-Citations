from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    """
    This function handles requests to the main page.
    It tells Flask to find and return the 'main-index.html' file
    from the 'templates' directory.
    """
    return render_template('main-index.html')

if __name__ == '__main__':
    """
    This block runs the web server when you execute the script directly.
    - debug=True allows for automatic reloading when you save changes.
    - port=5001 is used to avoid conflicts with other common applications.
    """
    print("Starting the RAG Citation App server...")
    print("Open your browser and navigate to http://127.0.0.1:5001")
    app.run(debug=True, port=5001)
