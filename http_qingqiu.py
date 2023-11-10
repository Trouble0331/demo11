# -*-coding:utf-8-*-
# @Time    :2023/10/2416:08
# @Author  :Trouble
# @Email   :651919278@qq.com
# @File    :http_qingqiu.py
# @Software:PyCharm

import requests


class HttpRequest:
    # 创建初始化函数，每次请求都需要提供URL和param两个必备参数
    def __init__(self, url, param):
        self.url = url
        self.param = param

    def http_request(self, method, cookies=None):  # 定义默认值

        if method.upper() == "GET":
            try:
                res = requests.get(self.url, self.param, cookies=cookies)
            except Exception as a:
                print("执行get 请求报错，错误是：{0}".format(a))

                res = "Error:get  请求报错{0}".format(a)
        elif method.upper == "POST":
            try:
                res = requests.post(self.url, self.param, cookies=cookies)
            except Exception as a:
                print("执行post 请求报错，错误是{0}".format(a))
                res = "Error:post 请求报错{0}".format(a)
        else:
                print("你的请求方式不对")
                res = "Error :请求方式不对报错{0}".format(method)
        return res