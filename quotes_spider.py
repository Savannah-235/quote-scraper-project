import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    # These paths are fixed cleanly to look at the real web server
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        # Loop through every single quote container box on the page
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get().replace("“", "").replace("”", "").strip(),
                "author": quote.css("small.author::text").get().strip(),
                "tags": "; ".join(quote.css("a.tag::text").getall()),
            }

        # Locates the path of the 'Next' page button you found in Safari!
        next_page = response.css("ul.pager li.next a::attr(href)").get()
        
        # If a next page exists, follow the link recursively
        if next_page:
            yield response.follow(next_page, callback=self.parse)
