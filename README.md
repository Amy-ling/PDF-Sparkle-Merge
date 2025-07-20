# ✨ PDF Sparkle Merge ✨

A privacy-focused PDF merging tool designed for local use. Your documents never leave your computer.

A simple yet stylish web application built with Flask to merge multiple PDF files into one. It features a modern, user-friendly interface with drag-and-drop support, file reordering, and a dark/light theme toggle.

## 🚀 Features

- **Merge Multiple PDFs**: Upload two or more PDF files to combine them.
- **Drag & Drop Interface**: Easily add files by dragging them into the drop zone.
- **Reorder Files**: Drag and drop the uploaded files to set the desired merge order.
- **Custom Filename**: Optionally specify a new name for the merged PDF. If no name is provided, a default name is generated from the uploaded files (e.g., `file1_file2_merged.pdf`).
- **Download Merged File**: Receive the merged PDF directly in your browser.
- **Responsive Design**: A clean UI that works on different screen sizes.
- **Dark Mode**: A toggle for a comfortable viewing experience in low-light environments.

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **PDF Manipulation**: PyPDF2
- **Frontend**: HTML, CSS, JavaScript
- **UI Features**:
    - Drag-and-drop and sorting powered by `Sortable.js`.
    - Theming and modern styling with custom CSS.
    - Dynamic UI updates with vanilla JavaScript.

## ⚙️ Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv .venv
    .venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application for development:**
    ```bash
    python app.py
    ```
    This is a development server. For production, see the deployment section below.

5.  Open your web browser and navigate to `http://127.0.0.1:5000`.

## 🚀 Deployment

The built-in Flask server (`python app.py`) is for development only. For a production environment, you should use a production-ready WSGI server. This project includes `waitress`.

To run the application with `waitress`, use the following command:
```bash
waitress-serve --host 127.0.0.1 --port 5000 app:app
```

## 📁 Project Structure

The project uses temporary directories for file handling, which are managed by the operating system and cleaned up automatically.

```
.
├── app.py              # Main Flask application logic
├── requirements.txt    # Python dependencies
├── static/
│   ├── style.css       # CSS for styling the frontend
│   └── js/
│       └── Sortable.min.js # JS for drag-and-drop
└── templates/
    └── index.html      # Main HTML template for the UI
```