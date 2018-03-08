import lxml.etree  
import sys  
import requests
  
html = ''''' 
<html> 
　　<head> 
　　　　<meta name="content-type" content="text/html; charset=utf-8" /> 
　　　　<title>友情链接查询 - 站长工具</title> 
　　　　<!-- uRj0Ak8VLEPhjWhg3m9z4EjXJwc --> 
　　　　<meta name="Keywords" content="友情链接查询" /> 
　　　　<meta name="Description" content="友情链接查询" /> 
 
　　</head> 
　　<body> 
　　　　<h1 class="heading">Top News</h1> 
　　　　<p style="font-size: 200%">World News only on this page</p> 
　　　　Ah, and here's some more text, by the way. 
　　　　<p>... and this is a parsed fragment ...</p> 
 
　　　　<a href="http://www.cydf.org.cn/" rel="nofollow" target="_blank">青少年发展基金会</a>  
　　　　<a href="http://www.4399.com/flash/32979.htm" target="_blank">洛克王国</a>  
　　　　<a href="http://www.4399.com/flash/35538.htm" target="_blank">奥拉星</a>  
　　　　<a href="http://game.3533.com/game/" target="_blank">手机游戏</a> 
　　　　<a href="http://game.3533.com/tupian/" target="_blank">手机壁纸</a> 
　　　　<a href="http://www.4399.com/" target="_blank">4399小游戏</a>  
　　　　<a href="http://www.91wan.com/" target="_blank">91wan游戏</a> 
       <div class="news"> 
        1. <b>无流量站点清理公告</b>  2013-02-22<br /> 
        取不到的内容11 
        </div> 
        <div class="news"> 
        2. <strong>无流量站点清理公告</strong>  2013-02-22<br />取不到的内容22 
        </div>  
        <div class="news"> 3. <span>无流量站点清理公告</span>  2013-02-22<br />取不到的内容33 
        </div>  
        <div class="news"> 4. <u>无流量站点清理公告</u>  2013-02-22<br />取不到的内容44 
        </div> 
    　　</body> 
</html> 
'''  

url = 'http://match.sports.sina.com.cn/iframe/football/team_iframe.php?id=52&year=2017&dpc=1'
content = requests.get(url);
print(content)