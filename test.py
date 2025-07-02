import requests
# File: test_whatsapp.py
import os 
print("Starting WhatsApp alert test...")

message = "TEST Alert from your application!"  # Default message
send_whatsapp_alert("7702853524", message)  # Replace with full international number

#whatsapp notifier function
def send_whatsapp_alert(number, message):
    """Send a WhatsApp message using local Node.js notifier."""
    try:
        res = requests.post("http://localhost:3000/send", json={
            "number": number,
            "message": message
        })
        if res.status_code == 200:
            print("WhatsApp alert sent.")
        else:
            print(f"WhatsApp alert failed: {res.text}")
    except Exception as e:
        print(f"Error sending WhatsApp alert: {e}")