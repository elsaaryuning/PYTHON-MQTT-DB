import paho.mqtt.client as mqtt
import mysql.connector

# Konfigurasi MQTT
mqttServer = "202.157.186.97"
mqttPort = 1883
mqttUser = "pablo"
mqttPassword = "costa"
topic = "sensor/data"

# Konfigurasi MySQL
db = mysql.connector.connect(
    host="127.0.0.1",        # Ganti dengan alamat host MySQL jika perlu
    user="root",        # Ganti dengan username MySQL
    password="", # Ganti dengan password MySQL
    database="sensor_db"     # Ganti dengan nama database
)
cursor = db.cursor()

# Fungsi untuk menyimpan data ke MySQL
def save_to_db(sensor_id, temperature, humidity):
    sql = "INSERT INTO sensor_data (sensor_id, temperature, humidity) VALUES (%s, %s, %s)"
    values = (sensor_id, temperature, humidity)
    cursor.execute(sql, values)
    db.commit()
    print(f"Data saved: {values}")

# Callback ketika menerima pesan
def on_message(client, userdata, message):
    payload = message.payload.decode('utf-8')
    print(f"Data received: {payload}")

    try:
        # Memisahkan data berdasarkan koma
        sensor_id, temperature, humidity = payload.split(',')
        save_to_db(sensor_id, float(temperature), float(humidity))
    except Exception as e:
        print(f"Error: {e}")

# Callback ketika berhasil terhubung ke broker MQTT
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker successfully!")
    else:
        print(f"Failed to connect, return code {rc}")

# Fungsi untuk subscribe dan menerima data
def subscribe():
    client = mqtt.Client()
    client.username_pw_set(mqttUser, mqttPassword)
    client.on_connect = on_connect  # Menambahkan callback on_connect
    client.connect(mqttServer, mqttPort)

    client.subscribe(topic)
    client.on_message = on_message

    print(f"Subscribed to topic: {topic}")
    client.loop_forever()

# Mulai subscriber untuk menerima data
subscribe()
