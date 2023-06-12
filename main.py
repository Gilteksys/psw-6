import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys
import subprocess
import threading

def start_django_server():
    subprocess.call(['python', 'manage.py', 'runserver'])

def open_browser():
    app = QApplication(sys.argv)

    # Crie uma instância do QWebEngineView
    webview = QWebEngineView()

    # Carregue a URL do seu aplicativo Django
    webview.load(QUrl("http://127.0.0.1:8000"))  # Substitua pela URL correta do seu servidor Django

    # Exiba a janela do QWebEngineView
    webview.show()

    sys.exit(app.exec_())

# Inicie o servidor Django em uma thread separada
django_thread = threading.Thread(target=start_django_server)
django_thread.start()

# Aguarde um breve momento para que o servidor Django seja iniciado
time.sleep(2)
# Abra o navegador para exibir a página de login
open_browser()











