import paho.mqtt.client as mqtt
import random
import time

# Konfigurasi MQTT
mqttServer = "202.157.186.97"
mqttPort = 1883
mqttUser = "pablo"
mqttPassword = "costa"
topic = "sensor/data"

# Fungsi untuk mengirim data ke MQTT Broker
def publish_data():
    client = mqtt.Client()
    client.username_pw_set(mqttUser, mqttPassword)
    client.connect(mqttServer, mqttPort)

    while True:
        # Data sensor acak
        sensor_id = "sensor_1"
        temperature = round(random.uniform(20.0, 30.0), 2)
        humidity = round(random.uniform(40.0, 60.0), 2)

        # Membuat payload data
        payload = f"{sensor_id},{temperature},{humidity}"
        client.publish(topic, payload)
        print(f"Data sent: {payload}")

        time.sleep(5)  # Mengirim data setiap 5 detik

# Memulai pengiriman data
publish_data()
