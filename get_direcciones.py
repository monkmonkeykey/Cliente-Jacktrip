import warnings
from urllib3.exceptions import NotOpenSSLWarning
warnings.filterwarnings("ignore", category=NotOpenSSLWarning)

import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth

# IP del TP-Link, según tu red
router_ip = "192.168.15.2"
router_url = f"http://{router_ip}/userRpm/AssignedIpAddrListRpm.htm"  # Ajusta si la ruta es distinta

username = "admin"         # Tu usuario
password = "AscoSpock1@" # Tu contraseña

try:
    response = requests.get(router_url, auth=HTTPBasicAuth(username, password), timeout=5)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        for row in soup.find_all("tr"):
            cols = row.find_all("td")
            if len(cols) >= 3:
                ip = cols[0].text.strip()
                mac = cols[1].text.strip()
                hostname = cols[2].text.strip()
                print(f"{ip} - {hostname} ({mac})")
    else:
        print(f"Error: Código de estado HTTP {response.status_code}")
except Exception as e:
    print(f"Error de conexión o autenticación: {e}")
