import requests
from lxml import etree
import json
from utils.sendNotify import send
msg = ''
url = "http://cs.xhu.edu.cn/1742/list.htm"
# http://cs.xhu.edu.cn/1742/list.htm
payload={}
headers = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
}
response = requests.request("GET", url, headers=headers, data=payload)
response.encoding = response.apparent_encoding
tree = etree.HTML(response.text)

name = tree.xpath('/html/body/div[3]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div[1]/table/tbody[1]/tr/td[1]/div/a/text()')[0]
time_text = tree.xpath('/html/body/div[3]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div[1]/table/tbody[1]/tr/td[2]/text()')
time = str(time_text[0]).replace(" ", "").replace("\r", "").replace("\n", "")
if time != '2023-06-19':
   msg += time
   msg += '\n'
   msg += name
   send(title='西华大学招生办', content=msg)


