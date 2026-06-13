import requests, re, sys
r = requests.get('https://proxybrazil.com/', headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
text = r.text
print("Page length:", len(text))
# find all img src
imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', text)
for img in imgs[:20]:
    print('img:', img)
# look for favicon
fav = re.findall(r'<link[^>]+rel=["\'](?:shortcut )?icon["\'][^>]+href=["\']([^"\']+)["\']', text)
for f in fav:
    print('favicon:', f)
