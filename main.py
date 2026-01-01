import qrcode

base_url = "https://ooonakooo.github.io/New_Year/"

links = {
    "бабушка": f"{base_url}?name=бабушка",
}

for name, url in links.items():
    img = qrcode.make(url)
    img.save(f"{name}.png")


