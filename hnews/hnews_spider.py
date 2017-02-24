import scrapy
import time
from send_email import send


class HnewsSpider(scrapy.Spider):
    name = 'hnewsspider'
    start_urls = ['https://news.ycombinator.com/']

    def __init__(self):
        self.post_list = []
        self.max_of_posts = 5

    def closed(self, reason):
        def to_html():
            html = ''
            for title, link in self.post_list:
                html += '<h2>' + str(title) + '</h2>'
                html += '<h3><a href="' + str(link) + '">' + str(link) + '</h3>'
            return html

        def send_email(message):
            subject = 'HackerNews - ' + str(time.strftime("%d/%m/%Y"))
            send(subject, message)

        html = to_html()
        send_email(html)

    def parse(self, response):
        for count, title in enumerate(response.css('.storylink')):
            link = title.css('a ::attr(href)').extract_first()
            if link:
                text_title = title.css('a ::text').extract_first()
                print(text_title)
                self.post_list.append((text_title, link))
            if count == self.max_of_posts:
                break
