from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os
#variavel responsavel por controlar o caminho do arquivo
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
#rota responsavel por carregar a pagina inicial
@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)
#rota responsavel por fazer o upload do arquivo
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and file.filename:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return index()
#rota responsavel pelos downloads dos arquivos salvos
@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
#iniciar a aplicação
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50000)
