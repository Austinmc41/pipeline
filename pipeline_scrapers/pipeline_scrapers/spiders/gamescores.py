from pathlib import Path
from typing import Iterable

import scrapy
from scrapy import Request


class GamescoresSpider(scrapy.Spider):
    name = "gamescores"
    allowed_domains = ["baseball-reference.com"]
    start_urls = ["https://www.baseball-reference.com/boxes/index.fcgi"]

    def start_requests(self) -> Iterable[Request]:
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url.split("/")[-2]
        file_name = f"Scores-{page}"
        game_summaries = response.css(".game_summaries")
        all_game_summaries = game_summaries.css("div.game_summary").getall()

        print(dict(all_game_summaries=all_game_summaries))
        # Path(file_name).write_bytes(game_summaries)
        # self.log(f"Saved file {file_name}")
