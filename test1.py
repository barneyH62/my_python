

import scrapy
import json
import pandas as pd
import datetime
import requests
import pprint

url = 'https://webapp.huolala.cn/index.php?_m=comm&_a=a_city_info&callback=callbackACityInfo&city_id=1671&_=1567087446229'
r = requests.post(url)
rS = r.text.replace('callbackACityInfo(', '').replace(')', '')
result = json.loads(rS)
print(result)
pprint.pprint(result)
city = result.get('data').get('name')
print(city)
rlist = result.get('data').get('vehicle_item')
for i in range(len(rlist)):
    tempr = rlist[i]
    print(tempr)
    print(tempr.get('name'))
    print(tempr.get('price_text_item').get('price_fen'))
    print(tempr.get('price_text_item').get('exceed_segment_price'))
    #





# for i in range(700):
#     cid = 1001
#     print(cid + i)
#     url = 'https://webapp.huolala.cn/index.php?_m=comm&_a=a_city_info&callback=callbackACityInfo&city_id=%s&_=1567087446229'%str(cid+i)
#
#     r = requests.post(url)
#     rS = r.text.replace('callbackACityInfo(', '').replace(')', '')
#     result = json.loads(rS)
#     # print(result)
#     # pprint.pprint(result)
#
#     try:
#         rlist = result.get('data').get('vehicle_item')
#         print(len(rlist))
#     except Exception as e:
#         print('没有该cityid')
#         continue


    # for i in range(7):
    #     print(rlist[i])
    # if len(rlist) == 0:
    #     print(cid+i)
        # break