import requests
import json

def clean_fact(text):
    # Remove CDATA or unwanted wrappers if needed
    return text.strip()

facts = []
for _ in range(7):
    r = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    if r.status_code == 200:
        fact = r.json().get("text", "")
        facts.append(clean_fact(fact))

# Save to JSON file
with open("facts.json", "w") as f:
    json.dump(facts, f, indent=2)
