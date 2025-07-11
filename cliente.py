import socket
import platform
from datetime import datetime
import json
import paho.mqtt.client as mqtt

# Función para obtener IP local
def get_local_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except:
        return "No se pudo obtener"

# Recolectar información
datos = {
    "hostname": socket.gethostname(),
    "ip_local": get_local_ip(),
    "sistema_operativo": platform.platform(),
    "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

# Convertir a JSON
mensaje = json.dumps(datos)

# Parámetros del broker MQTT local (ajusta si usas otro host)
broker = "192.168.15.20"  # IP del servidor MQTT
puerto = 1883
topico = "sistema/info"

# Publicar mensaje
cliente = mqtt.Client()
cliente.connect(broker, puerto, 60)
cliente.publish(topico, mensaje)
cliente.disconnect()

print("Mensaje enviado al broker MQTT.")
