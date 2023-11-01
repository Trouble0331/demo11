# -*-coding:utf-8-*-
# @Time    :2023/10/178:49
# @Author  :Trouble
# @Email   :651919278@qq.com
# @File    :parse_csv.py
# @Software:PyCharm



import csv
def parse_csv(file):
    mylist=[]

    with open(file,"r",encoding="utf-8") as f:
        data = csv.reader(f)
        for i in data:
            mylist.append(i)
        del mylist[0]
        return mylist

if __name__ == '__main__':
    data = parse_csv(r"D:\python\pycharm\test\unitest测试\po设计模块\testfenge.csv")
    print(data)