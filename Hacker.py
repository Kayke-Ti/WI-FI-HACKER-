import subprocess

wifi_name="FTTH"

results=subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi_name, 'key=clear']).decode('utf-8').split('/n')

results=[b.split(":")[1][1:-1] for b in results if "key Content" in b]

print("wifi name:+"wifi_name+" Password:"+results[0])