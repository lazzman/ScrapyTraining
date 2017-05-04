#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年5月4日

从 http://www.xicidaili.com/nn/1 网页上抓取国内高匿代理

xpath语法详见：
http://www.w3school.com.cn/xpath/index.asp
http://docs.pythontab.com/scrapy/scrapy0.24/topics/selectors.html#id2

Selector有四个基本的方法(点击相应的方法可以看到详细的API文档):
    xpath(): 传入xpath表达式，返回该表达式所对应的所有节点的selector list列表 。
    css(): 传入CSS表达式，返回该表达式所对应的所有节点的selector list列表.
    extract(): 序列化该节点为unicode字符串并返回list。
    re(): 根据传入的正则表达式对数据进行提取，返回unicode字符串list列表。


@author: NodCat
'''

import scrapy
from ScrapyTraining.items import ProxyIPItem

class XiciSpider(scrapy.Spider):
    '''
    name: 用于区别Spider。 该名字必须是唯一的，您不可以为不同的Spider设定相同的名字。
    start_urls: 包含了Spider在启动时进行爬取的url列表。 因此，第一个被获取到的页面将是其中之一。 后续的URL则从初始的URL获取到的数据中提取。
    parse() 是spider的一个方法。 被调用时，每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。 该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象。
    '''
    name = 'xici'
    allowed_domains = ["www.xicidaili.com"]
    start_urls = [
    #    "http://www.xicidaili.com/nn/1"
    ]

    def start_requests(self):
        for i in range(1, 3): # 取前两页，共200条代理
            url = 'http://www.xicidaili.com/nn/%d'%i
            req = scrapy.Request(url)
            yield req
    
    def parse(self, response):
        table = response.xpath('//table[@id="ip_list"]')[0] # 返回值是数组，取当中的第一个select对象
        trs = table.xpath('//tr')[1:] # 去除首行标题行
        for tr in trs:
            item = ProxyIPItem() # 创建item对象，item的使用类似dict
            item['ip'] = tr.xpath('td[2]/text()').extract()[0] # 提取内容   extract返回的结果是数组，所以[0]
            item['port'] = tr.xpath('td[3]/text()').extract()[0] # 提取内容   extract返回的结果是数组，所以[0]
            item['server_address'] = tr.xpath('td[4]/a/text()').extract()[0] # 提取内容   extract返回的结果是数组，所以[0]
            item['type'] = tr.xpath('td[6]/text()').extract()[0] # 提取内容   extract返回的结果是数组，所以[0]
            item['response_time'] = tr.xpath('td[7]/div/@title').extract()[0] # 提取内容   extract返回的结果是数组，所以[0]
            item['connect_time'] = tr.xpath('td[8]/div/@title').extract()[0] # 提取内容   extract返回的结果是数组，所以[0]
            item['alive_time'] = tr.xpath('td[9]/text()').extract()[0] # 提取内容   extract返回的结果是数组，所以[0]
            item['check_time'] = tr.xpath('td[10]/text()').extract()[0] # 提取内容   extract返回的结果是数组，所以[0]
            yield item
    