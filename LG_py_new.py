#python 3.6

import requests
import re
import os
import time
import sys
import datetime
import io
import logging

date = datetime.date.today()

def console_out(logFilename):
    ''''' Output log to file and console '''
    # Define a Handler and set a format which output to file
    logging.basicConfig(
        level=logging.ERROR,  # 定义输出到文件的log级别，大于此级别的都被输出
        format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s',  # 定义输出log的格式
        datefmt='%Y-%m-%d %A %H:%M:%S',  # 时间
        filename=logFilename,  # log文件名
        filemode='a+')  # 写入模式“w”或“a”
    # Define a Handler and set a format which output to console
    console = logging.StreamHandler()  # 定义console handler
    console.setLevel(logging.INFO)  # 定义该handler级别
    formatter = logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s  %(message)s')  # 定义该handler格式
    console.setFormatter(formatter)
    # Create an instance
    logging.getLogger().addHandler(console)  # 实例化添加handler

    # Print information              # 输出日志级别
    #logging.debug('logger debug message')
    #logging.info('logger info message')
    #logging.warning('logger warning message')
    logging.error('logger error message')
    logging.critical('logger critical message')

def get_info(type,w_type,city):

    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city='+city+'&needAddtionalResult=false'
    flag = 0
    a = 'a'
    b = 'b'
    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '43',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '_ga=GA1.2.1527602413.1523154566; user_trace_token=20180408102928-a9b14cdc-3ad4-11e8-b665-525400f775ce; LGUID=20180408102928-a9b150b4-3ad4-11e8-b665-525400f775ce; _gid=GA1.2.549101232.1523154566; LG_LOGIN_USER_ID=4252bc12ed7ecaa633a1c6e4e82bfe3a82fb7917c41f40b3e460b222b20daf23; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; index_location_city='+city+'; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22162a333752849e-0ec92ae2c10d8a-b34356b-1327104-162a3337529348%22%2C%22%24device_id%22%3A%22162a333752849e-0ec92ae2c10d8a-b34356b-1327104-162a3337529348%22%7D; sajssdk_2015_cross_new_user=1; JSESSIONID=ABAAABAABEEAAJACEB0215A69270A9E4C8E22A2F0349CCF; _gat=1; LGSID=20180408113541-e996bcad-3add-11e8-b674-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3Fpx%3Ddefault%26city%3D%25E5%258C%2597%25E4%25BA%25AC; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1523154566,1523154932,1523158539; _putrc=B02BCA36DD54FD83123F89F2B170EADC; login=true; unick=%E6%A2%81%E6%99%93%E5%A3%B0; gate_login_token=999aba3baef6137fab5e4c8161a0f357a93ae10da427829554e092278e20cb2f; LGRID=20180408114330-01384ae0-3adf-11e8-b677-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1523159008; SEARCH_ID=f2ed24e259bd4738bb6ff0a090197cda',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_'+w_type+'+?px=default&city='+city,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest'
      }
    for n in range(1,31):
        time.sleep(3)
        postData = {
                'first':'ture',
                'pn'   :str(n),
                'kd'   :type
           }
        html = requests.post(url, data=postData,headers = header)

        print(html)
        for m in range(len(html.json()['content']['positionResult']['result'])):
            companyFullName = html.json()['content']['positionResult']['result'][m]['companyFullName']
            if(flag == n+1):
                a = companyFullName
            if(flag == n):
                b = companyFullName
            if(a == b):
                break
            print(companyFullName)

            jobNature = html.json()['content']['positionResult']['result'][m]['jobNature']

            firstType = html.json()['content']['positionResult']['result'][m]['firstType']

            education = html.json()['content']['positionResult']['result'][m]['education']

            workYear = html.json()['content']['positionResult']['result'][m]['workYear']

            salary = html.json()['content']['positionResult']['result'][m]['salary']

            positionName = html.json()['content']['positionResult']['result'][m]['positionName']

            companySize = html.json()['content']['positionResult']['result'][m]['companySize']

            city0 = html.json()['content']['positionResult']['result'][m]['city']

            district = html.json()['content']['positionResult']['result'][m]['district']
            console_out('logging.log')
            financeStage = html.json()['content']['positionResult']['result'][m]['financeStage']
            #爬取时间处理
            formatCreateTime = html.json()['content']['positionResult']['result'][m]['formatCreateTime']
            formatCreateTime = data_process(formatCreateTime)
            console_out('logging.log')
            secondType = html.json()['content']['positionResult']['result'][m]['secondType']
            console_out('logging.log')
            #district = html.json()['content']['positionResult']['result'][m]['district']
            #district = html.json()['content']['positionResult']['result'][m]['district']
            file = open(str(date)+'.txt', 'a+',encoding='utf8')
            file.write(companyFullName+'\t')
            file.write(jobNature+'\t')
            file.write(education+'\t')
            file.write(workYear+'\t')
            file.write(salary+'\t')
            file.write(positionName+'\t')
            #file.write(companySize+'\t')
            file.write(city0+'\t')
            file.write(financeStage+'\t')
            file.write(firstType+'\t')
            file.write(formatCreateTime+'\n')
            file.close()

def data_process(formatCreateTime):
    now = datetime.date.today()
    s = re.search(r"发布",formatCreateTime)
    #print (s)
    if(s):
        if (formatCreateTime == '1天前发布'):
            data = datetime.timedelta(days=1)
            formatCreateTime = (now - data).strftime('%Y-%m-%d')
        elif (formatCreateTime == '2天前发布'):
            data = datetime.timedelta(days=2)
            formatCreateTime = (now - data).strftime('%Y-%m-%d')
        elif (formatCreateTime == '3天前发布'):
            data = datetime.timedelta(days=3)
            formatCreateTime = (now - data).strftime('%Y-%m-%d')
        else:
            formatCreateTime = now.strftime('%Y-%m-%d')
    else:
        n_now = str(now)
        data = formatCreateTime
        d1 = datetime.datetime.strptime(n_now,'%Y-%m-%d')
        d2 = datetime.datetime.strptime(data,'%Y-%m-%d')
        d = d1 - d2
        if(str(d) > '3 days, 0:00:00'):
            formatCreateTime = data
        else:
            formatCreateTime = now.strftime('%Y-%m-%d')

    return formatCreateTime

if __name__ == '__main__':
    Type_l = ['java', 'python', 'C++', 'C', '嵌入式','物联网','大数据']
    w_type = {'java':'java',
              'python':'python',
              'C++':'C%2B%2B',
              'C':'C',
              '嵌入式':'%E5%B5%8C%E5%85%A5%E5%BC%8F',
              '物联网':'%E7%89%A9%E8%81%94%E7%BD%91',
              '大数据':'%E5%A4%A7%E6%95%B0%E6%8D%AE%E3%80%81'
              }
    city = ['北京','上海','广州','深圳','杭州','成都','南京','武汉','西安','厦门','太原']
    City = {'北京':'%E5%8C%97%E4%BA%AC',
            '上海':'%E4%B8%8A%E6%B5%B7',
            '广州':'%E5%B9%BF%E5%B7%9E',
            '深圳':'%E6%B7%B1%E5%9C%B3',
            '杭州':'%E6%9D%AD%E5%B7%9E',
            '成都':'%E6%88%90%E9%83%BD',
            '南京':'%E5%8D%97%E4%BA%AC',
            '武汉':'%E6%AD%A6%E6%B1%89',
            '西安':'%E8%A5%BF%E5%AE%89',
            '厦门':'%E5%8E%A6%E9%97%A8',
            '太原':'%E5%A4%AA%E5%8E%9F'
            }

    print(date)
    a = 0
    filename = str(date)+'.txt'
    file = open(filename,'w',encoding='utf8')
    file.truncate()
    file.close()
    for j in range(len(city)):
        console_out('logging.log')
        for i in range(len(Type_l)):
            print(j,i)
            get_info(Type_l[i],w_type[Type_l[i]],City[city[j]])
            console_out('logging.log')
            if(i == 2 and j == 5):
                time.sleep(5)




