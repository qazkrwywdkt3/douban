# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    #爬虫名字
    name = 'douban_spider'
    #允许的域名
    allowed_domains = ['movie.douban.com']
    #入口
    start_urls = ['https://movie.douban.com/top250']
#默认解析方法
    def parse(self, response):
        #循环电影条目
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")

        for i_item in movie_list:
            #item文件导进来
            douban_item = DoubanItem()
            douban_item['序号'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['电影名称'] = i_item.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            content = i_item.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            for i_content in content:
                content_s = "".join(i_content.split())
                douban_item['电影介绍'] = content_s
            douban_item['星级'] = i_item.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//div[@class='star']/span[2]/text()").extract_first()
            douban_item['电影的评论数'] = i_item.xpath(".//div[@class='star']//span[4]/text()").extract_first()
            douban_item['电影描述'] = i_item.xpath(".//p[@class='quote']//span//text()").extract_first()
            print(douban_item)
            yield douban_item
            #解析下一页规则
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link,callback=self.parse)


