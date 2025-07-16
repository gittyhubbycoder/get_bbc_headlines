import requests, re, json

rss = requests.get("https://feeds.bbci.co.uk/news/rss.xml").text
titles = re.findall(r"<title>(.*?)</title>", rss)[1:6]
with open("headlines.json", "w") as f:
    json.dump({ "titles": titles }, f, indent=2)
