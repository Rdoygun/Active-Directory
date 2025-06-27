# 🕵‍♂ AD Domain Controller Finder

Basit ama etkili bir Python script'i: Active Directory ortamlarında domain controller'ları hızlıca bulur, IP'lerini çözer ve ping ile erişilebilirliklerini kontrol eder.

## 🚀 Özellikler

- _ldap._tcp.dc._msdcs.<domain> SRV sorgusu ile DC'leri listeler  
- Hostname’leri IP’ye çevirir  
- IP'lere ping atarak *aktif/pasif* durumlarını belirler  
- Çıktıları hem terminale hem de domain_controllers.txt dosyasına yazar

## 🔧 Gereksinimler

- Python 3
- Linux ortamı (ping için -c ve -W bayrakları kullanılıyor)

## ⚙ Kurulum

Herhangi bir bağımlılık yok. Dosyayı klonla veya indir, direkt çalıştır:

```bash
git clone https://github.com/Rdoygun/Active-Directory.git
cd Active-Directory
python3 DC_Finder.py 
