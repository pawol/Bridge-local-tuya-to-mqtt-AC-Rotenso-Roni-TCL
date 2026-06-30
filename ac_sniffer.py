import time
import tinytuya
import json

# --- TWOJE DANE POKÓJ ---
DEVICE_ID = "3776781148e7294d41c7"
DEVICE_IP = "192.168.2.45"
DEVICE_KEY = "MC[$r7[(p>mf8u^@"
# -------------------------

d = tinytuya.Device(DEVICE_ID, DEVICE_IP, DEVICE_KEY)
d.set_version(3.3)

print(">>> START SNIFFERA DPS (naciskaj przyciski na pilocie)\n")

last = {}

while True:
    try:
        status = d.status()
        dps = status.get("dps", {})

        # porównanie z poprzednim stanem
        for key, value in dps.items():
            if key not in last or last[key] != value:
                print(f"[ZMIANA] DPS {key}: {last.get(key)} -> {value}")

        last = dps

    except Exception as e:
        print("BŁĄD:", e)

    time.sleep(1)
