import paho.mqtt.client as mqttClient
import time
import faceRecognition as faceRecognition
import publisher as publisher

def on_connect(client, userdata, flags, rc):

    if rc == 0:
        print("Connected to broker")
        global Connected
        Connected = True

    else:
        print("Connection failed")

def on_message(client, userdata, message):
    print ("Message received:" , str(message.payload.decode("utf-8")))
    if message.payload.decode() == "Movement detected!":
            faceRecognition.main()
            publisher.main()

Connected = False

broker_address = "tailor.cloudmqtt.com"
port = 15628
user = "jswnyenq"
password = "UPt8dPRCjneU"

client = mqttClient.Client("Python70")
client.username_pw_set(user, password=password)
client.on_connect= on_connect
client.on_message= on_message

client.connect(broker_address, port=port)

client.loop_start()

while Connected != True:
    time.sleep(0.1)
    client.subscribe("sensor/movement")

try:
    while True:
        time.sleep(1)


except KeyboardInterrupt:
    print ("exiting")
    client.disconnect()
    client.loop_stop()
