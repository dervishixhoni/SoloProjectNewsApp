import urllib.request
import json 

input = "google"
# Bitcoin Genesis Block Transactions
your_url = f'https://newsapi.org/v2/top-headlines?q={input}&apiKey=bf1cb8dc1df74505a310b9dc5301942e'

with urllib.request.urlopen(your_url) as url:
    data = json.loads(url.read().decode())
    print(data['articles'])