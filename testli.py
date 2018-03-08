import os
import requests
import csv
from lxml import html,etree

headers = {
    'Host': 'match.sports.sina.com.cn'
    }


def save(writer,table):
    for item in table:
        writer.writerow(item)
    

def crawl(url):
    data = []
    r = requests.get(url,headers = headers)
    if r.encoding.find('ISO-8859') :
        encodings = requests.utils.get_encodings_from_content(r.text)
        if encodings:
            encoding = encodings[0]
    else:
       encoding = r.apparent_encoding
    page = r.content.decode(encoding, 'replace')
    root = etree.HTML(page)
    table = root.xpath('//tr')
    index = 0
    for item in table:
        row = [] 
        if index == 0:
            row = ['场次']
            row.extend(item.xpath('./th/text()'))
        
        else:       
            text = item.xpath('./td/text()')
            if text:
                row.append(text[0])   
                del text[0]
                teams = item.xpath('./td/a/text()')
                row.extend(teams)
                row.extend(text)
        data.append(row)
        index += 1
    return data

        
    

if __name__ == '__main__':
    with open('player.csv','w', newline = '',encoding = 'utf-8') as myfile:
        writer = csv.writer(myfile)
        url = 'http://match.sports.sina.com.cn/football/player_iframe.php?id=37265&season=2016&dpc=1'
        table = crawl(url)
        test_list = ['\t'.join(x) for x in table]
        myfile.writelines(test_list)
        save(writer,table)
     
 
