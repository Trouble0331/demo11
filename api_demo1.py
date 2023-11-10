# -*-coding:utf-8-*-
# @Time    :2023/10/2415:14
# @Author  :Ervin Chiu
# @Email   :ErvinChiu@outlook.com
# @File    :api_demo.py
# @Software:PyCharm

import requests

# get 请求

# res = requests.get("https://www.baidu.com")
# print(res)
# print(res.request.headers)
# print(res.status_code)

# http://150.109.156.47:8000/api/get_event_list/?eid=3


# url = "http://150.109.156.47:8000/api/get_event_list"
# param = {"eid": "3"}
# res = requests.get(url, param)
# print(res.json())


import unittest

from http_qingqiu import HttpRequest

#from ddt import ddt, data

#from do_excel import DoExcel

#
# class TestHttpRequest(unittest.TestCase):
#
#     def test_case_00(self):
#         url = "http://150.109.156.47:8000/api/get_event_list"
#         param = {"eid": "1"}
#         res = HttpRequest(url, param).http_request("get")
#         print("第1条用例的执行结果是：{0}".format(res.json()))
#
#     def test_case_01(self):
#         url = "http://150.109.156.47:8000/api/get_event_list"
#         param = {"eid": "2"}
#         res = HttpRequest(url, param).http_request("get")
#         print("第2条用例的执行结果是：{0}".format(res.json()))
#
#     def test_case_02(self):
#         url = "http://150.109.156.47:8000/api/get_event_list"
#         param = {"eid": "3"}
#         res = HttpRequest(url, param).http_request("get")
#         print("第3条用例的执行结果是：{0}".format(res.json()))
#
#     def test_case_03(self):
#         url = "http://150.109.156.47:8000/api/get_event_list"
#         param = {"eid": "6"}
#         res = HttpRequest(url, param).http_request("get")
#         print("第4条用例的执行结果是：{0}".format(res.json()))
#
#
# if __name__ == '__main__':
#     unittest.main()


# test_data = [{"url": "http://150.109.156.47:8000/api/get_event_list", "param": {"eid": "1"}, "method": "get"},
#              {"url": "http://150.109.156.47:8000/api/get_event_list", "param": {"eid": "2"}, "method": "get"},
#              {"url": 'http://150.109.156.47:8000/api/get_event_list', 'param': {'eid': "3"}, "method": "get"}]
#
#
# @ddt
# class TestHttpRequest(unittest.TestCase):
#
#     @data(*test_data)
#     def test_case_01(self, data_item):
#         print("**********" * 10)
#         print("ddt 分解出来的数据是：{0}".format(data_item))
#
#         res = HttpRequest(data_item["url"], data_item["param"]).http_request(data_item["method"])
#         print("第一条用例的执行结果是{0}".format(res.json()))
#
#
# if __name__ == '__main__':
#     unittest.main()


import pymysql
import logging

db = pymysql.connect(host="localhost", user="root", password="root", database="guest", charset="utf8")
cursor = db.cursor()
cursor.execute("select * from `datas`")

data = cursor.fetchall()
for i in data:
    print("ddt 分解出来的数据是：{0}".format(i))



class TestHttpRequest(unittest.TestCase):
    def setUp(self) -> None:
        pass


    def test_case_01(self):
        print("**********" * 20)
        for i in data:
            id = i[0]
            method = i[2]
            url = i[3]
            param = i[4]

            res = HttpRequest(url,eval(param)).http_request(method)
            print("第{1}条用例执行结果是{0}".format(res.json(),id))
            logging.getLogger().setLevel(logging.INFO)
            logging.info(
                f"case:添加发布会，发布会时间错误\n"
            )
            try:
                self.assertEqual(res.json()["status"], 10200)
                sql = f"UPDATE `datas` SET results = 'pass' where case_id={id}"
                cursor.execute(sql)
                db.commit()
                print("测试结果写入完毕!")

            except AssertionError as e:
                print("执行接口测试出错，错误是{0}".format(e))
                sql = f"UPDATE `datas` SET results = 'fail' where case_id={id}"
                cursor.execute(sql)
                db.commit()
                print("测试结果写入完毕!")


            finally:
                pass
    def tearDown(self) -> None:
        cursor.close()
        db.close()
        print("测试结束！")


if __name__ == '__main__':
    unittest.main()





# test_data = DoExcel(r"C:\Users\Trouble\Desktop\data.xlsx", "Sheet1").do_excel()


# @ddt
# class TestHttpRequest(unittest.TestCase):
#     def setUp(self) -> None:
#         self.t = DoExcel(r"C:\Users\Trouble\Desktop\data.xlsx", "Sheet1")
#
#     @data(*test_data)
#     def test_case_01(self, data_item):
#         print("**********" * 20)
#         print("ddt 分解出来的数据是：{0}".format(data_item))
#
#         res = HttpRequest(data_item["url"], eval(data_item["params"])).http_request(data_item["method"])
#         print("第{1}条用例执行结果是{0}".format(res.json(),data_item["id"]))
#         try:
#             self.assertEqual(res.json()["status"], 10200)
#
#             test_result = "Pass"
#         except AssertionError as e:
#             print("执行接口测试出错，错误是{0}".format(e))
#
#             test_result = "Fail"
#            # raise e
#
#         finally:
#                 self.t.write_back(data_item["id"] + 1, 7, str(res.json()))
#                 self.t.write_back(data_item["id"] + 1, 8,test_result)
#     def tearDown(self) -> None:
#         print("测试结束！")
#
#
# if __name__ == '__main__':
#     unittest.main()












# test_data = DoExcel(r"C:\Users\Trouble\Desktop\data.xlsx", "Sheet1").do_excel()
#
#
# @ddt
# class TestHttpRequest(unittest.TestCase):
#     def setUp(self) -> None:
#         self.t = DoExcel(r"C:\Users\Trouble\Desktop\data.xlsx", "Sheet1")
#
#     @data(*test_data)
#     def test_case_01(self, data_item):
#         print("**********" * 20)
#         print("ddt 分解出来的数据是：{0}".format(data_item))
#
#         res = HttpRequest(data_item["url"], eval(data_item["params"])).http_request(data_item["method"])
#         print("第一条用例的执行结果是{0}".format(res.json()))
#         try:
#             self.assertEqual(res.json()["status"], 10200)
#
#             test_result = "Pass"
#         except AttributeError as e:
#             print("执行接口测试出错，错误是{0}".format(e))
#
#             test_result = "Fail"
#         finally:
#
#             self.t.write_back(data_item['id'] + 1, 7, str(res.json()))
#             self.t.write_back(data_item['id'] + 1, 8, test_result)
#
#     def tearDown(self) -> None:
#         print("测试结束！")
#
#
# if __name__ == '__main__':
#     unittest.main()
