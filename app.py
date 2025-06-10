from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded = request.files.get('file')
    if not uploaded:
        return "No file uploaded", 400

    # Read spreadsheet into DataFrame
    try:
        df = pd.read_excel(uploaded)
    except Exception:
        df = pd.read_csv(uploaded)

    preview_html = df.head().to_html(index=False)
    return render_template('upload.html', preview=preview_html)

if __name__ == '__main__':
    app.run(debug=True)
