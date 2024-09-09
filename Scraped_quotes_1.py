from bs4 import BeautifulSoup
import requests
import csv
page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
quote = soup.find_all("span", attrs = {"class" : "text"})
authors = soup.find_all("small", attrs = {"class" : "author"})
file = open("scraped_quotes.csv", "w")
writer=csv.writer(file)
writer.writerow(["quote", "authors"])
for quotes,author in zip(quote,authors):
    print(quotes.text + "-" + author.text)
    writer.writerow([quotes.text, author.text])
file.close()
pip install pyinstaller