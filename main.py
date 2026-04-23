from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films"

response = requests.get(url, timeout=20)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table")

data = []
if table:
    for row in table.find_all("tr")[1:]:
        cols = row.find_all("td")
        if len(cols) >= 5:
            rank = cols[0].get_text(strip=True)
            title = cols[1].get_text(strip=True)
            year = cols[2].get_text(strip=True)
            rating = cols[3].get_text(strip=True)
            votes = cols[4].get_text(strip=True)
            data.append([rank, title, year, rating, votes])

df = pd.DataFrame(data, columns=["Rank", "Title", "Year", "Rating", "Votes"])
df.to_csv("top_100_films.csv", index=False)