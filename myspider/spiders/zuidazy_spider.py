import scrapy
import json
import codecs

# 最大资源网 scrapy_spider demo
class ZuidazySpider(scrapy.Spider):
    name = "zuidazy"
    start_urls = [
        'http://zuidazy.com/?m=vod-type-id-17-pg-1.html',
    ]

    def parse(self, response):
        myfile = codecs.open('urls.txt', 'wb', encoding='utf-8')
        for parent_dom in response.css('div.xing_vb'):
            myhref = parent_dom.xpath('ul/li/span/a/@href').extract()
            myfile.write(u'{myhref}\n'.format(myhref='\n'.join(myhref)))

