from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

# خواندن لینک vless اصلی
with open("کانفیگت بزار این تو.txt", "r", encoding="utf-8") as f:
    vless_link = f.read().strip()

# خواندن لیست IP ها
with open("آدرس آی پی.txt", "r", encoding="utf-8") as f:
    ips = [ip.strip() for ip in f if ip.strip()]

parsed = urlparse(vless_link)

uuid = parsed.username
port = parsed.port
query = parse_qs(parsed.query)

out = []

for i, ip in enumerate(ips, 1):
    # تغییر اسم کانفیگ
    fragment = f"IP-{i}"

    new_netloc = f"{uuid}@{ip}:{port}"

    new_query = urlencode(query, doseq=True)

    new_link = urlunparse((
        "vless",
        new_netloc,
        "",
        "",
        new_query,
        fragment
    ))

    out.append(new_link)

with open("آی پی های ساخته شدت اینجاس.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))

print("Done ✔")

print("""
🔥 The configurations are ready!
🎯 Now it's your turn to test them 😏
💻 Get ready, the world of VLESS is waiting!
""")
input("Press Enter when you're ready...")
