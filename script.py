import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import re

class Parser:
    def __init__(self, url):
        self.url = url
        self.data = []

    def fetch(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to fetch data: {response.status_code}")

    def parse(self, html):
        soup = BeautifulSoup(html, "html.parser")
        grid = soup.find("div", class_="letaky-grid")
        items = grid.find_all("div", class_="brochure-thumb")
        for item in items:

            title_element = item.find("p", class_="grid-item-content").find("strong")
            title = title_element.text.strip() if title_element else "Unknown Title"

            img_container = item.find("div", class_="img-container")
            if img_container:
                thumbnail = img_container.find("img")
                if thumbnail:
                    thumbnail = thumbnail.get("src") or thumbnail.get("data-src", "No Thumbnail")
                else:
                    thumbnail = "No Thumbnail"
            else:
                thumbnail = "No Thumbnail"

            shop_logo = item.find("div", class_="grid-logo")
            shop_name = shop_logo.find("img", alt=True)
            shop_name = shop_name["alt"].replace("Logo", "").strip() if shop_name else "Unknown Shop"
            
            date_range = item.find("small", class_="hidden-sm").text.strip()
            if " - " in date_range:
                valid_from, valid_to = date_range.split(" - ")
                valid_from = datetime.strptime(valid_from, "%d.%m.%Y").strftime("%Y-%m-%d")
                valid_to = datetime.strptime(valid_to, "%d.%m.%Y").strftime("%Y-%m-%d")
            elif "von" in date_range:
                valid_from = re.sub(r"von \w+", "", date_range).strip()
                valid_from = datetime.strptime(valid_from, "%d.%m.%Y").strftime("%Y-%m-%d")
                valid_to = "-"
            else:
                valid_from = "Unknown"
                valid_to = "Unknown"

            parsed_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.data.append({
                "title": title,
                "thumbnail": thumbnail,
                "shop_name": shop_name,
                "valid_from": valid_from,
                "valid_to": valid_to,
                "parsed_time": parsed_time
                })
    def save_to_json(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

def main():
    url = "https://www.prospektmaschine.de/hypermarkte/"
    parser = Parser(url)
    html = parser.fetch()
    parser.parse(html)
    parser.save_to_json("letaky.json")

if __name__ == "__main__":
    main()



# priklad divu s letkaom

#<div class="brochure-thumb col-xs-6 col-sm-3" data-brochure-id="331071" data-brochure-is-main="0" data-brochure-type="1">
#    <a href="/kaufland/umschlag-koln-von-donnerstag-13-03-2025-331071/" title="Vorschau von dem Prospekt des Geschäftes Kaufland, gültig ab dem 13.03.2025" data-brochure-id="331071"></a>
#    <div class="grid-item box blue ">
#        <a href="/kaufland/umschlag-koln-von-donnerstag-13-03-2025-331071/" title="Vorschau von dem Prospekt des Geschäftes Kaufland, gültig ab dem 13.03.2025" data-brochure-id="331071">
#            <div class="img-container">
#                <picture title=""><img class="" src="https://eu.leafletscdns.com/thumbor/M0UFd50qXoxZcr2VFXbR7pRdzhY=/full-fit-in/240x240/filters:format(webp):quality(65)/de/data/41/331071/0.jpg?t=1741504342" alt="Vorschau von dem Prospekt des Geschäftes Kaufland, gültig ab dem 13.03.2025"
#                        title="">
#                </picture>
#            </div>
#        </a>
#        <a href="/kaufland/umschlag-koln-von-donnerstag-13-03-2025-331071/" title="Vorschau von dem Prospekt des Geschäftes Kaufland, gültig ab dem 13.03.2025" onclick="" data-brochure-id="331071"></a>
#        <div class="letak-description">
#            <a href="/kaufland/umschlag-koln-von-donnerstag-13-03-2025-331071/" title="Vorschau von dem Prospekt des Geschäftes Kaufland, gültig ab dem 13.03.2025" onclick="" data-brochure-id="331071">
#                <div class="grid-logo">
#                    <picture class="ll loaded"><img class="" alt="Logo Kaufland" src="https://eu.leafletscdns.com/thumbor/DhwhEyF4R-jifJ3InKIsnWBUsDY=/full-fit-in/0x50/filters:format(webp):quality(65)/de/data/41/logo.png?4180406621339a240bb6d08c30728221"></picture>
#                </div>
#                <p class="grid-item-content"><strong>Umschlag - Köln</strong></p>
#                <p class="grid-item-content"><small class="hidden-sm">13.03.2025 - 19.03.2025</small><small class="visible-sm">13.03. - 19.03.2025</small></p>
#            </a>
#            <div class="grid-btns clearfix">
#                <a href="/kaufland/umschlag-koln-von-donnerstag-13-03-2025-331071/" title="Vorschau von dem Prospekt des Geschäftes Kaufland, gültig ab dem 13.03.2025" onclick="" data-brochure-id="331071"></a><a class="btn btn-alt btn-sm" href="/kaufland/umschlag-koln-von-donnerstag-13-03-2025-331071/" title="Vorschau von dem Prospekt des Geschäftes Kaufland, gültig ab dem 13.03.2025" style="display:block" data-brochure-id="331071">Zeige den Prospekt</a>
#            </div>
#        </div>
#    </div>
#</div>





