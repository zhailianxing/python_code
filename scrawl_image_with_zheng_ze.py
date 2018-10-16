from urllib import parse
from lxml import etree
import requests
import json
import re
from hashlib import md5
import requests


class GdtImage():
    def __init__(self):
        self.host = "http://test1-api-wailaxin-qukan.aimodou.net/"
        self.get_page_list_url = self.host + "api/gdtpage/getPageList"
        self.update_page_url  = self.host +  "api/gdtpage/updatePage"

    # 2. 爬取此url的 image, 计算md5值
    def demo_crawl(self, id, url):
        # url = 'http://tools.e.qq.com/pagemaker/page/preview?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJsYW5kaW5nX3BhZ2UiLCJpYXQiOjE1Mzk1OTU3MjQsImV4cCI6MTUzOTU5OTMyNCwiYSI6NzU2OTkyOCwibCI6IjIxMTk4OSIsInIiOjB9.aDKosX50t5-EBS8cvAprC5KawtkDKVouGVO6jUm2X6o'
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
        }
        res = requests.get(url, headers)
        print(type(res))
        print(res)

        # print("res.text:")
        # print(len(res.text))

        res = re.findall(r'window.pageData = (.*?);', res.text)
        try:
            url = json.loads(res[0]).get('components')[0].get('children')[0].get('image').get('url')
        except:
            print("id: url except:", id, url)
            return
        else:
            # url = url.replace('http:', '')
            # print(url)
            object = md5()
            # 将要生成hash值的数据更新进hash对象中
            object.update(url.encode('utf-8'))
            # 获取hash值
            sign = object.hexdigest()
            print(sign)

            data = {}
            data["id"] = id
            data["page_img"] = url
            data["page_img_md5"] = sign
            # 3. 更新接口
            self.update(data)


    def update(self, data):
        exit
        r = requests.post(self.update_page_url, data=data)
        print(r)

    # 1. 调用get接口 获取 id和url
    def get_page_list(self):
        print(self.get_page_list_url)
        res = requests.get(self.get_page_list_url)

        data = json.loads(res.text)
        if "data" in data:
            return data["data"]
        return []


if __name__ == '__main__':
    tmp =   GdtImage()
    # tmp.demo_crawl(url)
    exit()

    data = tmp.get_page_list()
    for item in data:
        print(item)
        id = item["id"]
        preview_url = item["preview_url"]
        if len(preview_url)>0:
            print("id:",id)
            tmp.demo_crawl(id, preview_url)
            # exit()




