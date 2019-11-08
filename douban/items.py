# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #序号
    序号 = scrapy.Field()
    #电影名称
    电影名称 = scrapy.Field()
    #电影介绍
    电影介绍 = scrapy.Field()
    #星级
    星级 = scrapy.Field()
    #电影的评论数
    电影的评论数 = scrapy.Field()
    #电影描述
    电影描述 = scrapy.Field()
