# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from shangraorenwucrawl.items import ShangraorenwucrawlItem

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['ren.bytravel.cn']
    start_urls = ['http://ren.bytravel.cn/Celebrity/index408_list.html']

    def parse(self, response):
        for sel in response.xpath('//table[@id="tjtable"]'):
        	# 这个table是索引页里每一个单位
        	# 这个表达式返回的是一个列表，所以可以for循环
        	item=ShangraorenwucrawlItem()
        	# 新建item对象
        	item['name']=sel.xpath('.//div[@id="tctitle"]//a[@class="blue14b"]/text()').extract()
        	item['time']=sel.xpath('.//div[@id="tctitle"]//a[@target="_blank"]/text()').extract()
        	item['birthYear']=sel.xpath('.//div[@id="tctitle"]/span[@class="bjc"]/a[1]/text()').extract()
        	item['intro']=sel.xpath('.//div[@id="tcjs"]/text()').extract()
        	# 用相对xpath地址爬取单元下的信息，相对xpath地址在前面加.
        	yield item
