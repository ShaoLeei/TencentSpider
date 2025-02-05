# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名称
    work_name = scrapy.Field()
    # 职位类别
    work_type = scrapy.Field()
    # 工作国家
    work_country = scrapy.Field()
    # 工作城市
    work_place = scrapy.Field()
    # 发布时间
    work_time = scrapy.Field()
    # 招聘链接
    work_link = scrapy.Field()

    # 职责
    work_duty = scrapy.Field()
    # 要求
    work_requir = scrapy.Field()
