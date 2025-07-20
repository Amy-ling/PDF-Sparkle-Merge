from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
from PyPDF2 import PdfMerger
import os
import tempfile
import time
import atexit
import shutil

app = Flask(__name__)
UPLOAD_FOLDER = tempfile.mkdtemp()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Schedule the cleanup of the temporary directory
atexit.register(lambda: shutil.rmtree(UPLOAD_FOLDER))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge_pdfs():
    files = request.files.getlist('pdfs[]')
    if len(files) < 2:
        return jsonify({'error': 'Please upload at least 2 PDF files'}), 400

    merger = PdfMerger()
    saved_files = []
    
    # Get the desired filename from the request, with a fallback
    custom_filename = request.form.get('filename', f'merged_{int(time.time())}.pdf')
    # Sanitize it one last time on the server
    final_filename = secure_filename(custom_filename)
    if not final_filename.lower().endswith('.pdf'):
        final_filename += '.pdf'


    for file in files:
        if file.filename.endswith('.pdf'):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], f"{int(time.time())}_{filename}")
            file.save(filepath)
            merger.append(filepath)
            saved_files.append(filepath)

    merged_path = os.path.join(app.config['UPLOAD_FOLDER'], final_filename)
    merger.write(merged_path)
    merger.close()

    # Clean up individual files
    for f in saved_files:
        os.remove(f)

    return send_file(merged_path, as_attachment=True, download_name=final_filename)

if __name__ == '__main__':
    app.run(debug=True)
