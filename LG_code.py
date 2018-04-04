#python3.6
import requests
import time
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
                   'kd': type}
        # 提交参数到服务器，返回数据信息---》招聘信息
        html = requests.post(url, data = postData, headers = header)
        print(html)
        for m in range(len(html.json()['content']['positionResult']['result'])):
           companyFullName =  html.json()['content']['positionResult']['result'][m]['companyFullName']
            #信息写入文件
           ff = open('ff.txt','a+')
           ff.write(companyFullName+'\n')

if __name__== '__main__':
    ff = open('ff.txt', 'a+')
    ff.write('\n'+"-----------------python----------------" + '\n')
    ff.close()
    type = 'python'
    get_info(type)
    ff = open('ff.txt', 'a+')
    ff.write('\n'+"-----------------java----------------" + '\n')
    ff.close()
    type = 'java'
    get_info(type)
    ff = open('ff.txt', 'a+')
    ff.write('\n'+"-----------------c----------------" + '\n')
    ff.close()
    type = 'c'
    get_info(type)