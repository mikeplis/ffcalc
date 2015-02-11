import scrapy
from ffcalc.items import FfcalcPick

class FfcalcSpider(scrapy.Spider):
    name = "ffcalc"
    allowed_domains = ["http://fantasyfootballcalculator.com/"]
    start_urls = [
        "http://fantasyfootballcalculator.com/draft/2566640"
    ]

    def parse(self, response):
        filename = "2566640"
        all_picks = response.xpath("//tbody/tr/td")
        for pick in all_picks:
            ffcalcPick = FfcalcPick()
            d = pick.xpath('text()')
            if len(d) == 3:
                ffcalcPick['first_name'] = d[0].extract().strip()
                ffcalcPick['last_name'] = d[1].extract().strip()
                yield ffcalcPick
