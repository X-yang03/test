# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import sys
import re
import requests
import pandas as pd

# def getData(url):
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'
#     }
#     req = urllib.request.Request(url=url, headers=headers, method="POST")
#     response = urllib.request.urlopen(req)
#     print(response.read().decode("utf-8"))
#     return response

# path="D:\\Doubancomments\\"
# os.makedirs(path)

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'
    }
Cookie = {'Cookie':'ll="118373"; bid=nwUzagXYPW0; __yadk_uid=6Acgns8MqIiVX8xdeR9XdvZpeZvyU70n; _vwo_uuid_v2=DA4FF1A9A542C586225D4F1CACD8FC1A2|a655a1bb3709fcf4e62213c6e574c19e; __gads=ID=bc89a11f4804e4d2-2224f02426c60020:T=1614221468:RT=1614221468:S=ALNI_MZuqSQCNFE-Xy2UlpFwBX1rX5jbnw; _vwo_uuid_v2=DA4FF1A9A542C586225D4F1CACD8FC1A2|a655a1bb3709fcf4e62213c6e574c19e; __utma=30149280.1421230719.1614221458.1617012037.1617347693.6; __utmc=30149280; __utmz=30149280.1617347693.6.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1617347695%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utmb=30149280.3.10.1617347693; __utma=223695111.243723590.1614221458.1617347695.1617347921.6; __utmb=223695111.0.10.1617347921; __utmz=223695111.1617347921.6.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_id.100001.4cf6=4453b42a3b7f578e.1614221457.5.1617348789.1617007153.'}

url_1 = "https://movie.douban.com/subject/35267208/comments?start="
url_2 = "&limit=20&sort=new_score&status=P&sort=new_score"

i=0
MaxPage=2
while i<MaxPage:
    # 拼接url
    # 当i=0时
    url = url_1+str(i*20)+url_2
    print(url)

    try:
        # request请求
        html = requests.get(url, headers=headers, cookies=Cookie)
        # Beautifulsoup解析网址
        soup = BeautifulSoup(html.content, 'lxml')
        print(html)

        use_name_list = soup.find_all('span', attrs={'class': 'comment-info'})
        # 评论文本
        comment_list = soup.find_all('span', attrs={'class': 'short'})
        # 评分
        rating_list = soup.find_all('span', attrs={'class': re.compile(r"allstar(\s\w+)?")})

        for r in range(len(use_name_list)):
            data1 = [
                (
                use_name_list[r].a.string,
                comment_list[r].string,
                rating_list[r].get('class')[0][7])
            ]
            data2 = pd.DataFrame(data1,columns =["用户名", "评论", "打分"])
            data2.to_csv('wanderingEarth_comments.csv', header=False, index=False, mode='a+',encoding="utf-8-sig")
        print('page '+str(i+1)+' has done')
    except:
        # 如出现异常，则出现error
        print("error!")
    i = i+1



print("Done!")




