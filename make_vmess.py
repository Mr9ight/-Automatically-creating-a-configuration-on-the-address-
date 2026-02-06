import base64
import json

with open("کانفیگت بزار این تو.txt", "r") as f:
    vmess_link = f.read().strip()

vmess_json = json.loads(
    base64.b64decode(vmess_link.replace("vmess://", "")).decode()
)

with open("آدرس آی پی.txt", "r") as f:
    ips = [ip.strip() for ip in f if ip.strip()]

out = []

for i, ip in enumerate(ips, 1):
    cfg = vmess_json.copy()
    cfg["add"] = ip
    cfg["ps"] = f"IP-{i}"

    encoded = base64.b64encode(
        json.dumps(cfg, separators=(",", ":")).encode()
    ).decode()

    out.append("vmess://" + encoded)

with open("آی پی های ساخته شدت اینجاس.txt", "w") as f:
    f.write("\n".join(out))

print("Done ✔")
🔥 The configurations are ready!
🎯 Now it's your turn to test them 😏
💻 Get ready, the world of VMESS is waiting!
""")
input("Press Enter when you're ready...")