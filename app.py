#coding:utf8
from datetime import datetime
import os,time,json
from flask import Flask, request,jsonify
from flask import render_template
from flask_cors import CORS
#in procfile to specify the python run the app
#web: FLASK_APP = server.py python -m flask run --host=0.0.0.0 --port=$PORT
app = Flask(__name__)
import ast
from translate import trans

CORS(app)
@app.route("/geoinfo")
def hello():
    a= [{"lat":'21.145',"lng":'14.534',"info":'swimming'},
{"lat":'62.145',"lng":'24.534',"info":'travel'},
{"lat":'53.145',"lng":'34.534',"info":'travle'},
{"lat":'44.145',"lng":'74.534',"info":'photography'},
{"lat":'35.145',"lng":'54.534',"info":'house'}]
    return json.dumps({"task":a})
    #return "Hello World!"




'''
from suds.client import Client

cc = Client('http://47.100.170.38:7789/?wsdl')
result = cc.service.say_hello()

print(result)
'''
@app.route("/map")
def mp():
    cc = Client('http://47.100.170.38:7789/?wsdl')
    result = cc.service.say_hello()
    print(type(result))
    b = ast.literal_eval(result)
    return json.dumps(b)


@app.route("/geo")
def mp1():
    #cc = Client('http://47.100.170.38:7789/?wsdl')
    #result = cc.service.say_hello()
    return render_template("map.html")


@app.route("/geoinfo")
def gyi():
    print("i am visiting remote server")
    return json.dumps({"task":[{"lat":'21.145',"lng":'34.534',"info":'swimming'}]})

@app.route("/trans")
def translate1():
    content = request.args.get('content')
    print(content)
    answer = trans(content)
    return answer


import chatbot
@app.route("/r1/chatbot")
def chat():
    content = request.args.get('content')
    answer = chatbot.get_answer(content)
    if  u'你好' in content:
        answer = u'你好我是沙盘精灵有什么可以帮你'
    if  u'帮助' in  content:
        answer ='我能给你介绍电商沙盘的一些基本功能,如介绍一些常见的规则，介绍一些常见的角色，介绍一些常见的策略，和一些电商相关的评价。'

    if u'电商沙盘' in content:
	answer = u'电商沙盘是一款帮助电商教学的多点触摸互动软件'
    if u'最美' in content:
        answer = u'胡乙凡'
    if u'最帅' in content:
        answer =  u'杨明'
    if u'提示'  in content:
        answer = u'你可以像这样提问？什么是电子商务？电商沙盘一些常见的功能？上海的天气,现在是什么时间？'
    if u'搜索引擎竞价' in content:
        answer  = u'搜索引擎竞价又称竞价排名，是一种按效果付费的网络推广方式，是把企业的产品、服务等通过以关键词的形式在百度搜索引擎平台上作推广。它是一种按效果付费的新型而成熟的搜索引擎服务，用少量的投入就可以给企业带来大量潜在客户，有效提升企业销售额。竞价排名是一种按效果付费的网络推广方式，由百度在国内率先推出。企业用最高的单次点击价格在搜索引擎上竞得一个关键词，当消费者在搜索引擎上搜索该关键词时，企业的推广信息就会率先出现在消费者相应的搜索结果中，如果该消费者点击了企业的搜索链接访问企业的网站，那么企业就要按照竞价的数额向搜索引擎支付相应的费用'


    if u'流量规则' in  content:
        answer = u'整个市场的流量规则包含了整体流量市场的变化，网站流量的争夺，注册用户的争夺' 
    if u'资产负债表' in content:
        answer =  '资产负债表表示企业在一定日期（通常为各会计期末）的财务状况（即资产、负债和业主权益的状况）的主要会计报表。资产负债表利用会计平衡原则，将合乎会计原则的资产、负债、股东权益”交易科目分为“资产”和“负债及股东权益”两大区块，在经过分录、转帐、分类帐、试算、调整等等会计程序后，以特定日期的静态企业情况为基准，浓缩成一张报表。其报表功用除了企业内部除错、经营方向、防止弊端外，也可让所有阅读者于最短时间了解企业经营状况。' 
    if u'资产负债表' in content and u'内容' in content:
        answer =  '资产负债表根据资产、负债、所有者权益(或股东权益，下同)之间的勾稽关系，按照一定的分类标准和顺序，把企业一定日期的资产、负债和所有者权益各项目予以适当排列。它反映的是企业资产、负债、所有者权益的总体规模和结构。即，资产有多少；资产中，流动资产、固定资产各有多少；流动资产中，货币资金有多少，应收账款有多少，存货有多少，等等。所有者权益有多少；所有者权益中，实收资本(或股本，下同)有多少，资本公积有多少，盈余公积有多少，未分配利润有多少，等等.https://wiki.mbalib.com/wiki/%E8%B5%84%E4%BA%A7%E8%B4%9F%E5%80%BA%E8%A1%A8'   



    if u'核心' in content:
	answer = u'多点触摸沙盘一体机的核心是基于光波的多点触摸技术，它能够扫描用户通过手指等传导的多重位置信息，并迅速将位置信息发送给系统软件，通过解析就可以知道用户的点击位置和具体手势'


    if u'多点触摸沙盘' in content:
        answer = u'多点触摸沙盘一体机是一种借助多点触摸技术改善传统上机实验、实训枯燥乏味现状的新一代人机交互设备'


    if u'互动教学'    in content:
        answer  = u'在教学中教与学双方交流、沟通、协商、探讨，在彼此平等、彼此倾听、彼此接纳、彼此坦诚的基础上，通过理性说服甚至辩论，达到不同观点碰撞交融，激发教学双方的主动性，拓展创造性思维，以达到提高教学效果的一种教学方式'
    
    if  u'沙盘精灵'    in   content or u'功能' in  content:
        answer  =  '我可以对你提出的关于电商沙盘以及一些常见对话做出回答'
    if  u'互动式教学'  in content:
        answer = "互动式教学被西方国家普遍采用和推崇，并形成主题探讨法、启发思考法、问题归纳法、案例分析法、情景创设法、多维思辨法等一系列的教学方法"
    if u'域名拍卖'  in content:
        answer = "域名拍卖是指通过竞价的方式进行域名交易，在规定的时间内买家各自出价，截止至域名拍卖时间结束，出价最高者得标，须以所出价向卖家购买此拍卖域名。"
    if u'光棍节'  in content:
        answer =  "在现实中，光棍节是每年11月11日，而在电子商务沙盘中，光棍节发生在第十一回合时。当光棍节到来的前一个回合，系统会提醒所有团队光棍节的到来。届时商品属性中与光棍节相关的商品就会热卖，即周转率大幅提升，同时市场的流量增长率会大幅提升，而由于配送压力增加甚至爆仓，会发生快递涨价事件，与配送相关的满意度也会下降，从而产生类似投诉。"
    if  u'国庆节'   in content:
       answer =  "在电子商务沙盘中，国庆节发生在第十个回合时。当国庆节到来的前一个回合，系统会提醒所有团队国庆节的到来。届时商品属性中与国庆节相关的商品就会热卖，即周转率大幅提升，同时市场的流量增长率会大幅提升，而由于配送压力增加甚至爆仓，会发生快递涨价事件，与配送相关的满意度也会下降，从而产生类似投诉。由于国庆长假持续时间长，因此相关指标增长情况要显著很多。"
    if u'春节'   in content:
       answer = "在电子商务沙盘中，春节发生在第十四个回合时。当春节到来的前一个回合，系统会提醒所有团队春节的到来。届时商品属性中与春节相关的商品就会热卖，即周转率大幅提升，同时市场的流量增长率会大幅提升，但同时所有员工工资、物流成本（不论自建或是外包）都是大幅上升，整体服务质量也会下降。"

    if u'网络营销' in content:
       answer = '常见的网络营销方式有域名拍卖，搜索引擎竞价，网络目录竞价'
   
    if u'网络目录竞价' in content:
       answer = '网络目录也称为网络资源目录或网络分类目录，是目录型网络检索工具。最早的网络目录是由人工采集网络上的网站（或网页），然后按照一定分类标准，如学科类型、主题等，建立网站分类目录，并将筛选后的信息分门别类放入各类目中供用户进行浏览，并辅助一定的检索。网络目录可以帮助用户自动导航到各种热门网站上，常常被用户设置为自己浏览器的默认主页，由此而诞生了一批拥有大量固定用户的网络目录。尽管网络目录不能替代搜索引擎的功能，但它给电子商务企业带来的流量却不容小视。网络目录可以放置的用于企业广告的“位置”毕竟有限，因此需要“价高者得”。' 



     
     

    print(content)
    return  json.dumps({'as':answer}) 
   



@app.route("/r1/robot")
def robot():
    return render_template("wechat.html")








if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)

