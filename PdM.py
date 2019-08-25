import uuid
from firebase import firebase
firebase = firebase.FirebaseApplication('https://xxxxxxxxx.firebaseio.com/', None)
import paho.mqtt.client as mqtt

mqtt_user_name = 'oauth2-user'
mqtt_password = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xxxxxxxxxxxxxxxJfbmFtZSI6Im5la2lhcnkwN0BnbWFpbC5jb20iLCJzY29wZSI6WyJyZWFkLW9ubHkiXSwiZXhwIjoxNjI4NTEyNDYzLCJhdXRob3JpdGllcyI6WyJST0xFX1VTRVIiXSwianRpIjoiZGYxN2MxMDctMTZjOS00NWY4LTlhYzktNDc1Mjg5YzIyMjk1IiwiY2xpZW50X2lkIjoicmVhZC1vbmx5In0.OwNii06ZqQTvwtx30Mb8NXXSIKpn-ynGQeS8-65iiwc'  # copy and paste here external access token from your account
user_id = 'xxxx'  # copy and paste here your user id
device_id = 'TO136-02xxxxxx10010F5'  # copy and paste here your device id


norm_datasource_topic= '/v1/users/{user_id}/in/devices/{device_id}/datasources/PDM_EVENT'.format(user_id=user_id,device_id=device_id)#PdM alerts

ca_cert_path = 'cacert.crt'



def on_connect(client, userdata, flags, rc):
    print('PdM'.format(code=rc))

def on_message(client, userdata, msg):
      print(str(msg.payload))
      x=str(msg.payload).split(',')[2].split(':')[1]
      firebase.put('status',"event",x)


def main():
    client = mqtt.Client(client_id=str(uuid.uuid4()), transport='websockets')
    
    
    client.on_connect = on_connect
    client.on_message = on_message

    client.tls_set(ca_certs="C:/Users/Admin/Desktop/cacert.crt")
    client.username_pw_set(mqtt_user_name, mqtt_password)

    client.connect('ns01-wss.brainium.com', 443)

    client.subscribe(norm_datasource_topic)#pdm events
    client.loop_forever()
    

if __name__ == "__main__":
    main()
