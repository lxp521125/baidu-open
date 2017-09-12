# -*- coding: utf-8 -*-
import requests
# 引入NLP SDK
from aip import AipNlp
from config import *

# 初始化AipNlp对象
aipNlp = AipNlp(APP_ID, API_KEY, SECRET_KEY)

def qinggan(title):
    result = aipNlp.sentimentClassify(title)
    print(result)

def toword(title):
    # result = aipNlp.dnnlm(title)
    result = aipNlp.lexer(title)
    # result = aipNlp.sentimentClassify(title)
    print(result)
    # url = "http://apis.baidu.com/apistore/pullword/words"
    # headers = { "apikey" : "02b4266363907681c6582d605b6dabb1" }
    # # req = urllib.request.Request(url, 'data', headers)
    # params = { "source": title, "param1" : 0.8, "param2" : 1}
    # response = requests.get(url, params = params , headers = headers)
    # the_page = response.text.encode('utf-8')
    # print(the_page)
    # if len(the_page)>300:
    #     return
    # new_s = the_page.split()
    # for i in new_s:
    #     print(i)

if __name__ == '__main__':
    # toword("""  扫描二维码登录微信. 登录手机微信. 手机上安装并登录微信. 从“发现”，进入“扫一扫”，扫码登录微信网页版. 扫描成功. 请在手机上点击确认以登录.一款跨平台的通讯工具。支持单人、多人参与。通过手机网络发送语音、 图片、视频和文字。微信公众平台,给个人、企业和组织提供业务服务与用户管理能力的全新服务平台。
    # 运营中心 辟谣中心 腾讯客服联系邮箱侵权投诉
    # 微信电脑版是腾讯为超过三亿人 使用的微信的用户开发的一款PC微信版本，微信电脑版官方下载版是最新的微信网页版，本站提
    # 群聊,也能视频聊天。 请在电脑访问 pc.weixin.qq.com 下载下载 微信PC版官方QQ群交流 145378303
    # 7 Tencent All Rights Reserved...Scan to log in to WeChat Log in on phone to use WeChat on Web  QR Code expired,Click Refresh  Scan successful Confirm login on mobile WeChat Switch...
    # 微信电脑版是由腾讯官方推出的一款跨平台的通讯工具。微信电脑版最初的版本是微信网页版，随之升级开发为客户端的形式，...
    # 微信网页版是电脑使用微信的方法,基本功能同微信一样,微信网页版无法访问朋友圈和使用微信的一些插件。微信网页版除了聊天之外,
    # 网页版微信的功能还包括:手机和电脑 """)
    qinggan("爱奇艺")