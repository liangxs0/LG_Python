#python3.6
import requests
import time
import xlwt
from xlrd import open_workbook
import os
from os.path import join
from xlutils.copy import copy
from datetime import datetime




def set_style(font_name, font_height, bold=False):
    style = xlwt.XFStyle()

    font = xlwt.Font()
    font.name = font_name  # 'Times New Roman'
    font.height = font_height
    font.bold = bold
    font.colour_index = 4

    borders = xlwt.Borders()
    borders.left = 6
    borders.right = 6
    borders.top = 6
    borders.bottom = 6

    style.font = font
    style.borders = borders
    return style

#建表函数
def write_to_excel_xlwt():
    '''Write content to a new excel'''
    row = 0
    lin = 0
    new_workbook = xlwt.Workbook()
    new_sheet = new_workbook.add_sheet("LG")
    # write cell with style
    style0 = set_style('Times New Roman',200,200)
    new_sheet.write(0, 0, 'companyFullName',style0)
    new_sheet.write(0, 1, 'jobNature',style0)
    new_sheet.write(0, 2, 'firstType',style0)
    new_sheet.write(0, 3, 'education',style0)
    new_sheet.write(0, 4, 'workYear',style0)
    new_sheet.write(0, 5, 'salary', style0)
    new_sheet.write(0, 6, 'positionName',style0)
    new_sheet.write(0, 7, 'companySize',style0)
    new_workbook.save(r"LG数据信息.xls")  # if change to xlsx,then open failed
def get_info(type):
    #获取网址信息
    url = "https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0"
    #反爬措施
    header = {  'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Length': '26',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': 'user_trace_token=20171115230713-fea80f9e-ac4b-40fe-a277-536d29d13770; LGUID=20171115230714-a98b0069-ca16-11e7-98f7-5254005c3644; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=475; index_location_city=%E5%8C%97%E4%BA%AC; _ga=GA1.2.1122313095.1510758424; _gid=GA1.2.1822026674.1521883771; JSESSIONID=ABAAABAAAIAACBIF7DF9D14D2BB87D5E2A735EC1F4F598E; LGSID=20180324184737-c4ba9952-2f50-11e8-b606-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521713574,1521794666,1521883771,1521888340; _putrc=D76A82F6EBE1BB5D; login=true; unick=%E6%9D%8E%E6%B5%B7%E5%AE%BD; gate_login_token=df83ba5b3b81e72aa7cd1c69048fd86f1a7b21c21ca43af6; SEARCH_ID=015c0e21f33b4f26930a71a6a3469a54; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521888473; LGRID=20180324184950-13bc131e-2f51-11e8-9b5f-525400f775ce; TG-TRACK-CODE=search_code',
                'Host': 'www.lagou.com',
                'Origin': 'https://www.lagou.com',
                'Pragma': 'no-cache',
                'Referer': 'https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
                'X-Anit-Forge-Code': '0',
                'X-Anit-Forge-Token': 'None',
                'X-Requested-With': 'XMLHttpRequest'}

    for n in range(30):
        time.sleep(1.5)
        #提交数据
        postData = {'first':'false',
                   'pn': str(n),
                   'kd': type
                    }
        # 提交参数到服务器，返回数据信息---》招聘信息
        html = requests.post(url, data = postData, headers = header)
        print(html)
        for m in range(len(html.json()['content']['positionResult']['result'])):
            companyFullName =  html.json()['content']['positionResult']['result'][m]['companyFullName']
            jobNature = html.json()['content']['positionResult']['result'][m]['jobNature']
            firstType = html.json()['content']['positionResult']['result'][m]['firstType']
            education = html.json()['content']['positionResult']['result'][m]['education']
            workYear = html.json()['content']['positionResult']['result'][m]['workYear']
            salary = html.json()['content']['positionResult']['result'][m]['salary']
            positionName = html.json()['content']['positionResult']['result'][m]['positionName']
            companySize = html.json()['content']['positionResult']['result'][m]['companySize']
            ff=open('ff.txt','a+')
            ff.write(companyFullName+'\n')
            ff.write(jobNature+'\n')
            ff.write(firstType + '\n')
            ff.write(education+'\n')
            ff.write(workYear+'\n')
            ff.write(salary+'\n')
            ff.write(positionName+'\n')
            ff.write(companySize+'\n')
            ff.close()
def index_data(row,line,con):
    source = r"‪G:\python_work\LG_data\LG数据信息.xls"
    rb = open_workbook("LG数据信息.xls",formatting_info=True)
    w = copy(rb)
    w.get_sheet(0).write(row,line,con)
    time.sleep(0.5)
    w.save("LG数据信息.xls")
if __name__== '__main__':

    i = 1
    j = 1
    b = 1
    a = 0
    c = 0
    if(j == 0):
        write_to_excel_xlwt()

    if (i==0):
        type = 'python'
        get_info(type)

        type = 'java'
        get_info(type)

        type = 'c'
        get_info(type)
    file = open("ff.txt","rU")
    count = len(file.readlines())
    file.close()
    print(count)

    file = open("ff.txt")
    for a in range(count+1):
        if (b > count//8):
            break
        line = file.readline()
        print ( b, c)
        index_data(b,c,line)
        print(line)
        c = c + 1
        if(c == 8):
            c = 0
            b = b+1

    file.close()
