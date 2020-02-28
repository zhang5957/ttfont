import requests
from lxml import etree
import re
from fontTools.ttLib import TTFont
import random
import time
# 获取详情页
def request_url(html):
    dds = html.xpath("//dl[@class='board-wrapper']")
    for dd in dds:
        ur = dd.xpath(".//a/@href")[0]
        detail_url = 'https://maoyan.com' + ur
        print(detail_url)
        time.sleep(1)
        parse_detail_url(detail_url)
        break

# 解析详情页
def parse_detail_url(detail_url):

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
        'Host': 'maoyan.com',
        'Cache-Control': 'max-age=0',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie':'__mta=20296455.1582441415981.1582695192905.1582695221534.38; uuid_n_v=v1; uuid=978AD020560A11EAA66B67143BC1537D0D3F54B197124C5F947F32FD9A753959; _csrf=37f48881fcd6cdea4105154a8fb375e3c7f3a3724cb966e0df3826a622955c2e; _lxsdk_cuid=17070dbc3c8c8-0eb98ad253ecdd-313f68-144000-17070dbc3c8c8; _lxsdk=978AD020560A11EAA66B67143BC1537D0D3F54B197124C5F947F32FD9A753959; mojo-uuid=561f782c14adf52867665b99041239c4; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=20296455.1582441415981.1582459005353.1582459011049.9; lt=eA_gEhN8aJ75Kta8MwkJ_B6sQjMAAAAAEQoAAEDjT5JSHWCTq2qnDgSWXu9oQeUmEgjQuFqEgQCW0KIC1O2gSStDkfw6hWck5oIyXA; lt.sig=Bx9rOhKg_tj_2LKjR9yKomX7oH0; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1582535974,1582535988,1582536078,1582536081; mojo-session-id={"id":"9455181570c4618137b5e80c34104047","time":1582695146986}; mojo-trace-id=5; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1582695221; _lxsdk_s=1707ffb661b-e95-57a-3a6%7C%7C9'
    }
    api_url = 'https://dps.kdlapi.com/api/getdps/?orderid=938252073467227&num=10&pt=1&format=json&sep=1'
    proxy_ip = requests.get(api_url).json()['data']['proxy_list']
    username = '595707874'
    password = '166mogtv'
    proxies = {
        "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {'user': username, 'pwd': password,'proxy': random.choice(proxy_ip)},
        "https": "https://%(user)s:%(pwd)s@%(proxy)s/" % {'user': username, 'pwd': password,'proxy': random.choice(proxy_ip)}
    }
    # 访问详情页
    resp = requests.get(detail_url, headers=headers, proxies=proxies)
    text = resp.text
    detail = etree.HTML(text)
    with open('替换前的网页.html','w',encoding='utf-8') as f:
        f.write(text)
    # 获取本地字体文件
    font1 = TTFont('字体文件.woff')  # 打开本地字体文件
    obj_list1 = font1.getGlyphNames()[1:-1]  # 获取所有字符的对象，去除第一个和最后一个
    uni_list1 = font1.getGlyphOrder()[2:]       #获取所有编码，去除前2个
    dict = {
        'uniE0C2':'1',
        'uniF5AE':'2',
        'uniF621':'3',
        'uniE87F':'4',
        'uniE77D':'5',
        'uniF4FA':'6',
        'uniE067':'7',
        'uniE572':'8',
        'uniEC17':'9',
        'uniF6FC':'0'
    }
    item = {}
    list1 = []
    for uni in uni_list1:
        print(uni)
        a = font1['glyf'][uni].flags
        b = list(a)
        print(b)
        print("--" * 40)
        list1.append(b)
    """
    16,25,16 | 10,32,0,20,16,5,28,30,27,22(0的个数)
    """
    item = {
        'uniE067': list1[0],'uniE572': list1[1],'uniE87F': list1[2],'uniF6FC': list1[3],'uniE77D': list1[4],'uniE0C2': list1[5],'uniF4FA': list1[6],'uniEC17': list1[7],'uniF621': list1[8],'uniF5AE': list1[9]
    }
    # 下载实时字体文件
    fonturl = re.findall("url\('//vfile.meituan.net/colorstone/(.+?)'\) format\('woff'\)",text)[0]
    print(fonturl)
    font_response = requests.get('https://vfile.meituan.net/colorstone/' + fonturl)
    with open("字体文件3.woff","wb") as fp:
        fp.write(font_response.content)
    font2 = TTFont('字体文件3.woff')
    font2.saveXML('字体文件3.xml')
    obj_list2 = font2.getGlyphNames()[1:-1]
    uni_list2 = font2.getGlyphOrder()[2:]
    item2 = {}
    list2 = []
    print(uni_list2[1])
    for uni2 in uni_list2:
        print(uni2)
        q = font2['glyf'][uni2].flags
        w = list(q)
        print(w)
        # print("--"*40)
        list2.append(w)
    item1 = {
        uni_list2[0]: list2[0],
        uni_list2[1]: list2[1],
        uni_list2[2]: list2[2],
        uni_list2[3]: list2[3],
        uni_list2[4]: list2[4],
        uni_list2[5]: list2[5],
        uni_list2[6]: list2[6],
        uni_list2[7]: list2[7],
        uni_list2[8]: list2[8],
        uni_list2[9]: list2[9]
    }
    print("开始比对。。。。。")
    for value in item.values():
        x = value.count(0)
        for value2 in item1.values():
            y = value2.count(0)
            if x == y:
                # 打印出需要查找的字体编号
                rep = list(item1.keys())[list(item1.values()).index(value2)]
                # 打印出基准文字的编号
                # print(list(item.keys())[list(item.values()).index(value)])
                res = list(item.keys())[list(item.values()).index(value)]
                result = dict[res]
                print(result)
                rep2 = rep.split('i')[1]
                rep3 = rep2.lower()
                print(rep3)
                detail_page = detail.replace('&#x'+str(rep3)+';', result)
                print("--" * 40)
            else:
                continue

    # items = {}
    # # 电影名字
    # name = detail.xpath("//div[@class='movie-brief-container']/h1/text()")[0]
    # category = detail.xpath("//li[@class='ellipsis']/a/text()")
    # # 电影分类
    # categorys = ''.join(category)
    # details = detail.xpath("//li[@class='ellipsis']/text()")
    # # 上映日期
    # date = details[-1]
    # times = details[-2].strip()
    # # 电影时长
    # time = re.sub("[\s/]",'',times)
    # rank = detail.xpath("//span[class='index-left info-num']/span/text()")
    # print(rank)




def main():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
        'Upgrade-Insecure-Requests':'1',
        'Sec-Fetch-Dest': 'document'
    }
    for x in range(0,10):
        url = 'https://maoyan.com/board/4?offset=%d' % (x*10)
        api_url = 'https://dps.kdlapi.com/api/getdps/?orderid=938252073467227&num=10&pt=1&format=json&sep=1'
        proxy_ip = requests.get(api_url).json()['data']['proxy_list']
        username = '595707874'
        password = '166mogtv'
        proxies = {
            "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {'user': username, 'pwd': password,'proxy': random.choice(proxy_ip)},
            "https": "https://%(user)s:%(pwd)s@%(proxy)s/" % {'user': username, 'pwd': password,'proxy': random.choice(proxy_ip)}
        }
        resp = requests.get(url,headers=headers,proxies=proxies)
        txt = resp.text
        html = etree.HTML(txt)
        time.sleep(1)
        request_url(html)
        break



if __name__ == '__main__':
    main()