#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# author: sunboy_2050
# blog: http://blog.mimvp.com
 
from selenium import webdriver
import time


import sys
reload(sys)
sys.setdefaultencoding('utf8')
 


# #生成一个文件名字符串  
# def generateFileName(): 
#   return str(uuid.uuid1()) 

# #根据文件名创建文件  
# def createFileWithFileName(localPathParam,fileName): 
#   totalPath=localPathParam+'\\'+fileName 
#   if not os.path.exists(totalPath): 
#     file=open(totalPath,'a+') 
#     file.close() 
#     return totalPath 
   
 
# #根据图片的地址，下载图片并保存在本地  
# def getAndSaveImg(imgUrl): 
#   if( len(imgUrl)!= 0 ): 
#     fileName=generateFileName()+'.jpg' 
#     urllib.urlretrieve(imgUrl,createFileWithFileName(localPath,fileName)) 
 
# #下载函数 
# def downloadImg(url): 
#   urlList=getUrlList(url) 
#   for urlString in urlList: 
#     getAndSaveImg(urlString) 
     

def spider_url_content(url):
    try:
        browser = webdriver.Firefox()       # 打开 FireFox 浏览器
     
#         chromeDriverDir = '/usr/bin/google-chrome'
#         browser = webdriver.Chrome(executable_path=chromeDriverDir)        # 打开 Chrome 浏览器
     
        # browser.implicitly_wait(10)  
        # 设置窗口大小
        # browser.set_window_size(1200,900)   
        browser.get(url)  
    #   content = browser.find_element_by_id('container')       # 通过标记id 获取网页的内容
    #   content = content.text
    #   滚动到页面底部－－该方案欠妥当
        # js="var q=document.documentElement.scrollTop=10000"
        # browser.execute_script(js)


        browser.execute_script("""
            (function (){
                var y = 0;
                var step = 100;
                window.scroll(0,0);

                function f(){
                    if(y < document.body.scrollHeight){
                        y+= step;
                        window.scroll(0,y);
                        setTimeout(f,100);
                    }else{
                        window.scroll(0,0);
                        document.title += "scroll-done";
                    }
                }
                setTimeout(f,1000);
            })();
        """)

        for i in xrange(30):
            if "scroll-done" in browser.title:
                    break
            time.sleep(10)

        browser.save_screenshot('test.png')
        browser.quit()                      # 关闭浏览器
         
     #   print("content: " + content)
         
    except Exception as ex:
        print("error msg: " + str(ex))
 
if __name__ == '__main__':
    url = 'https://www.jd.com'
    localPath='/Users/geliang/Desktop/selenium'
    spider_url_content(url)


