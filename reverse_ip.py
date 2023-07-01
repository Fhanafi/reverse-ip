import socket

def reverse_ip(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        reversed_ip = '.'.join(ip_address.split('.')[::-1])
        return reversed_ip
    except socket.gaierror:
        return "Tidak dapat menemukan IP untuk domain tersebut."

def reverse_ips_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            domains = file.readlines()
            domains = [domain.strip() for domain in domains]
            reversed_ips = [reverse_ip(domain) for domain in domains]
            return reversed_ips
    except FileNotFoundError:
        return "File tidak ditemukan."
    except IOError:
        return "Terjadi kesalahan saat membaca file."

def save_to_file(data, file_path):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(item + '\n')
        return "Data berhasil disimpan dalam file."
    except IOError:
        return "Terjadi kesalahan saat menyimpan file."
file_path = input("Masukkan path file: ")
reversed_ips = reverse_ips_from_file(file_path)
if isinstance(reversed_ips, list):
    print("Daftar:")
    for ip in reversed_ips:
        print(ip)
    
    reversed_ips_file_path = "reversed_ips.txt"
    save_result = save_to_file(reversed_ips, reversed_ips_file_path)
    print(save_result)
else:
    print(reversed_ips)
