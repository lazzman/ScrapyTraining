# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapytrainingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ProxyIPItem(scrapy.Item):
    '''
    Item 是保存爬取到的数据的容器；其使用方法和python字典类似， 并且提供了额外保护机制来避免拼写错误导致的未定义字段错误。
    '''
    ip = scrapy.Field() # ip
    port = scrapy.Field() # port
    server_address = scrapy.Field() # server_address
    type = scrapy.Field() # type http/https
    response_time = scrapy.Field() # response_time 响应时间越小越好
    connect_time = scrapy.Field() # connect_time 连接时间越小越好
    alive_time = scrapy.Field() # alive_time 存活时间
    check_time = scrapy.Field() # check_time 最后一次校验时间
