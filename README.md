# Top 100 Most Highly-Ranked Films Scraper

A Python web scraping project that collects data on the 100 most highly-ranked films from an archived EverybodyWiki page and exports the results to a CSV file.

## Project Structure

```
top-100-films/
├── main.py
├── top_100_films.csv
├── .gitignore
└── README.md
```

## Data Source

The data is scraped from a archived snapshot of the EverybodyWiki page:
[100 Most Highly-Ranked Films](https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films)

## Dataset

The generated CSV (`top_100_films.csv`) contains **108 rows** and the following columns:

| Column | Description |
|--------|-------------|
| `Rank` | Overall ranking of the film |
| `Title` | Title of the film |
| `Year` | Release year |
| `Rating` | Rating from a specific ranking list (may be `unranked`) |
| `Votes` | Vote count or position from another ranking source (may be `unranked`) |

## Requirements

- Python 3.7+
- `beautifulsoup4`
- `requests`
- `pandas`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AliIhsan020/top-100-films.git
   cd top-100-films
   ```

2. Install dependencies:
   ```bash
   pip install beautifulsoup4 requests pandas
   ```

   Or using a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   pip install beautifulsoup4 requests pandas
   ```

## Usage

Run the scraper:
```bash
python main.py
```

The script will fetch the data and save it as `top_100_films.csv` in the same directory.

## How It Works

1. Sends an HTTP GET request to the archived Wikipedia mirror page.
2. Parses the HTML using BeautifulSoup.
3. Locates the first `<table>` element on the page.
4. Iterates over each row and extracts 5 columns: Rank, Title, Year, Rating, Votes.
5. Stores the data in a pandas DataFrame and exports it to CSV.

## Notes

- Some entries have `unranked` as their Rating or Votes value, meaning the film did not appear in that particular ranking list.
- The scraper targets a static archived page, so results are deterministic and will not change over time.

---

## Türkçe Özet

Bu proje, EverybodyWiki sitesinin arşivlenmiş bir sayfasından **en yüksek puanlı 100 filmin** verisini çeken basit bir Python web kazıyıcısıdır.

`main.py` betiği; `requests` ile sayfayı indirir, `BeautifulSoup` ile HTML tablosunu ayrıştırır ve sonuçları `pandas` aracılığıyla `top_100_films.csv` dosyasına kaydeder. CSV dosyasında filmin sıralaması, adı, yapım yılı, puanı ve oy sayısı yer almaktadır. Bazı filmlerin puan veya oy sütunlarında `unranked` (sıralanmamış) değeri bulunabilir.
