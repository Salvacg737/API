# -*- coding: utf-8 -*-
import scrapy
from ..items import ProductItem
from MainApp.models import ProductinModels

class CurrysSpider(scrapy.Spider):
    name = 'Currys'
    start_urls = ['https://www.currys.co.uk/gbuk/search-keywords/xx_xx_xx_xx_xx/-clearance-/xx-criteria.html?ntid=B~d~Clearance']

    def parse(self, response):

        ProductInstance = ProductItem()

        brand = response.xpath('//span[@data-product="brand"]//text()').getall()

        ProductInstance['BrandinModels'] = brand

        yield ProductInstance