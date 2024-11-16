import paho.mqtt.client as mqtt
import time

# Detail koneksi MQTT
mqtt_server = "202.157.186.97"
mqtt_port = 1883
mqtt_user = "pablo"
mqtt_password = "costa"
mqtt_topic = "test/topic"

# Inisialisasi client MQTT
client = mqtt.Client()
client.username_pw_set(mqtt_user, mqtt_password)

# Menghubungkan ke broker
client.connect(mqtt_server, mqtt_port, 60)

# Mengirim pesan ke topik
message = input("Masukkan pesan yang ingin dikirim: ")
client.publish(mqtt_topic, message)

# Memberikan waktu agar pesan terkirim sebelum disconnect
time.sleep(2)

# Disconnect
client.disconnect()
