import requests, re, json

rss_url = "https://feeds.bbci.co.uk/news/rss.xml"
rss = requests.get(rss_url).text

# Extract titles using regex
titles = re.findall(r"<title>(.*?)</title>", rss)[1:8]  # Skip the first <title> (BBC News - Home)
print("I'm running!!!")
# Save to JSON
with open("deploy/bbc.json", "w", encoding="utf-8") as f:
    json.dump({"titles": titles}, f, indent=2)
