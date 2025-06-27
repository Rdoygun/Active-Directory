import subprocess
import re
import socket

def get_domain_controllers(domain):
    query = f"_ldap._tcp.dc._msdcs.{domain}"
    try:
        result = subprocess.run(
            ["nslookup", "-type=SRV", query],
            capture_output=True, text=True
        )
        output = result.stdout
        fqdn_list = re.findall(r"service = \d+ \d+ \d+ ([\w\.-]+)", output)
        return fqdn_list
    except Exception as e:
        print(f"[!] Hata oluştu: {e}")
        return []

def resolve_ip(fqdn):
    try:
        return socket.gethostbyname(fqdn)
    except socket.gaierror:
        return None

def is_alive(ip):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except:
        return False

def main():
    domain = input("Domain adını gir (örnek: example.local): ").strip()
    print("\n[•] Domain Controller'lar tespit ediliyor...\n")

    fqdns = get_domain_controllers(domain)
    output_lines = []

    if not fqdns:
        line = "[-] Hiçbir domain controller bulunamadı."
        print(line)
        output_lines.append(line)
    else:
        for fqdn in fqdns:
            ip = resolve_ip(fqdn)
            if ip:
                status = "aktif" if is_alive(ip) else "pasif"
                line = f"{fqdn} = {ip} [{status}]"
            else:
                line = f"{fqdn} = IP çözümlenemedi"
            print(line)
            output_lines.append(line)

    with open("domain_controllers.txt", "w") as f:
        f.write("\n".join(output_lines))
        f.write("\n")

    print("\n[✓] Çıktı domain_controllers.txt dosyasına yazıldı.")

if __name__ == "__main__":
    main()
