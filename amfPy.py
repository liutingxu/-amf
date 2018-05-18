import pyamf
#import urllib as ub
import urllib.request as ub
import http.cookiejar as hc
import time
import requests as re
import uuid  
import pyamf  
from pyamf import remoting  
from pyamf.flex import messaging
import time
import datetime
import json
import datetime  
  
class DateEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, datetime.datetime):  
            return obj.strftime('%Y-%m-%d %H:%M:%S')  
        elif isinstance(obj, date):  
            return obj.strftime("%Y-%m-%d")  
        else:  
            return json.JSONEncoder.default(self, obj) 



#http://w
#获取首页
def getPage(userName, passWord):
    
    url = "网址"

    cookie = hc.CookieJar()  # 声明一个CookieJar对象实例来保存cookie
    handler = ub.HTTPCookieProcessor(cookie)  # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    opener = ub.build_opener(handler)  # 通过handler来构建opener
    ub.install_opener(opener)
    response = ub.urlopen(url)  # 此处的open方法同urllib2的urlopen方法，也可以传入request

    jsessionid = "";
    for item in cookie:
        if item.name == "JSESSIONID":
            jsessionid=item.value.strip()
        #print('Name = ' + item.name)
        #print('Value = ' + item.value)
    #print(response)
    #print(response.url)
    url = "网址";
    url = 网址参数拼接;

    
    response = ub.urlopen(url);
    #for item in cookie:
        #print('Name = ' + item.name)
        #print('Value = ' + item.value)
    #print(response);
    #print(response.url);
    list1 = [''];
    #基本信息
    basicList = getAmf(list1, 'qxxxxxxx', 'inxxxxxxer', jsessionid, opener)
    #医保
    medicalList = getAmf(list1, 'qxxxxxxx01', 'inxxxxxxger', jsessionid, opener)
    #养老
    list1=['参数1', '199001', '209912']
    ylList = getAmf(list1, 'quxxxxxxx001', 'infxxxxxxxer', jsessionid, opener)
    #应缴实缴queryAc20ByAac001
    list1=['参数1', "'11','12','14','15','21','31','32','33','35','36','41','51','61','1','2','3','4','5','302','301'", "'10','20'", "'0','1'", '199001',  '209912', False]
    needPay = getAmf(list1, 'qxxxxxxxxxc001', 'infoxxxxxxager', jsessionid, opener)
    list1=['参数1']
    pPay = getAmf(list1, 'qxxxxxxxd', 'inxxxxxxxger', jsessionid, opener)
    #print(pPay)
    dic = {'basic': basicList, 'medical': medicalList, 'yl': ylList, 'needPay': needPay, 'pPay' : pPay}
    #print(repr(dic))
    json_str = json.dumps(dic, cls=DateEncoder)
    #json1 = json.dumps(pPay, cls=DateEncoder)
    #print(json1)
    print(json_str)
    

def getCookie(userName, passWord):
    url = "网址"
    url = 参数拼接;
    request = ub.Request(url)
    set_cookie = ub.urlopen(request).info()['Location']
    print(set_cookie)


def getHis(userName, passWord):
     url = "网址"
    url = 参数拼接;
    r = re.get(url)
    cookies = r.request._cookies
    for item in cookies:
        print('Name = ' + item.name)
        print('Value = ' + item.value)
    print(r.history)
    print(r.url)
    print(r.cookies)
    r = re.get(123123123")
    print(r.request)
    print(r.read())

def getAmf(list1, operationStr, destinationStr, jsessionid, opener):
    list = []
    #list1 = [''];
    # 构造flex.messaging.messages.RemotingMessage消息
    #print(str(uuid.uuid1()).upper())
    msg = messaging.RemotingMessage(messageId=str(uuid.uuid1()).upper(),  
                                clientId=None,  
                                operation=operationStr,  
                                destination=destinationStr,  
                                timeToLive=0,  
                                timestamp=0);
    # 第一个是查询参数
    msg.body = list1
    msg.headers['DSEndpoint'] = 'my-amf'  
    msg.headers['DSId'] = str(uuid.uuid4()).upper()
    # 按AMF协议编码数据  
    req = remoting.Request('null', body=(msg,))  
    env = remoting.Envelope(amfVersion=pyamf.AMF3)  
    env.bodies = [('/1', req)]  
    data = bytes(remoting.encode(env).read())
    url="123123123"
    t = time.time();
    headC = "Hm_lvt_447d5331c7cf0d9e38c7ee579499d9fb=" + str(int(t)) + ";Hm_lpvt_447d5331c7cf0d9e38c7ee579499d9fb" + str(int(t)) + ";JSESSIONID=" + jsessionid;
    
    req = ub.Request(url,data, headers={'Content-Type': 'application/x-amf', 'Cookie': headC, 'Accept':'*/*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN',
   'Host': '1111111',
   'Pragma': 'no-cache',
   'Proxy-Connection': 'Keep-Alive',
   'Referer': '1111111111111111111',
   'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; wbx 1.0.0)',
   'x-flash-version': '29,0,0,113'})
    resp = remoting.decode(opener.open(req).read())
    #for i, record in enumerate(resp.bodies[0][1].body.body[0]):
        #print(record)
    #print(resp)
    a = resp.bodies[0][1].body.body['resultList'];
    #print(a)
    #print(a.get(8));
    #for record in a:
        #list.append(a);
        #print(record)
    return a;




getPage("账号","密码")


#B0830435985C53216C898E04DEAA0D0C89B527A79EE94EB4A333CA5FAA3BD686

#7f766phsSaIwrflZrcqP3P74Bck3jeN91nW-V-1bcD_bT8g1hXFx!663673290
