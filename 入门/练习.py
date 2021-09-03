''' 练习：简易日志分析 '''
web_log = [
    '123.125.71.69,-,-,[24/Jun/2019:11:23:00,+0800],https,www.domain.com,443,"GET,/article-132050-1.html,HTTP/1.1",200,48425,"-","Mozilla/5.0 (compatible;Baiduspider/2.0;+http://www.baidu.com/search/spider.html)","-",0.210,0.210,2019-06-24T11:23:00+08:00,TLSv1.2',
    '220.181.108.161,-,-,[24/Jun/2019:12:08:00,+0800],https,www.domain.com,443,"GET,/thread-23019-1-1.html,HTTP/1.1",200,1551,"-","Mozilla/5.0 (compatible;;Baiduspider/2.0;+http://www.baidu.com/search/spider.html)","-",0.062,0.062,2019-06-24T12:08:00+08:00,TLSv1.2',
    '111.206.198.97,-,-,[24/Jun/2019:12:08:01,+0800],https,www.domain.com,443,"GET,/thread-23019-1-1.html?_dsign=1b1af586,HTTP/1.1",200,71861,"https://www.798wd.com/thread-23019-1-1.html","Mozilla/5.0 (compatible;Baiduspider-render/2.0;+http://www.baidu.com/search/spider.html)","-",0.147,0.147,2019-06-24T12:08:01+08:00,TLSv1.2',
    '220.181.108.176,-,-,[24/Jun/2019:14:03:59,+0800],https,www.domain.com,443,"GET,/thread-154156-1-1.html,HTTP/1.1",200,1784,"-","Mozilla/5.0 (compatible;Baiduspider/2.0;+http://www.baidu.com/search/spider.html)","-",0.061,0.061,2019-06-24T14:03:59+08:00,TLSv1.2',
    '111.206.198.123,-,-,[24/Jun/2019:14:04:04,+0800],https,www.domain.com,443,"GET,/thread-154156-1-1.html?_dsign=489d02b9,HTTP/1.1",200,65541,"https://www.798wd.com/thread-154156-1-1.html","Mozilla/5.0 (compatible;Baiduspider-render/2.0;+http://www.baidu.com/search/spider.html)","-",0.145,0.145,2019-06-24T14:04:04+08:00,TLSv1.2',
    '123.125.71.89,-,-,[24/Jun/2019:14:30:17,+0800],https,www.domain.com,443,"GET,/sitemap35.xml,HTTP/1.1",200,1600112,"-","Mozilla/5.0 (compatible;Baiduspider/2.0;+http://www.baidu.com/search/spider.html)","-",0.115,-,2019-06-24T14:30:17+08:00,TLSv1.2',
    '123.125.71.32,-,-,[24/Jun/2019:16:20:37,+0800],https,www.domain.com,443,"GET,/article-25-1.html,HTTP/1.1",200,1762,"-","Mozilla/5.0 (compatible;Baiduspider/2.0;+http://www.baidu.com/search/spider.html)","-",0.059,0.059,2019-06-24T16:20:37+08:00,TLSv1.2',
    '123.125.71.33,-,-,[24/Jun/2019:17:57:26,+0800],https,www.domain.com,443,"GET,/sitemap47.xml,HTTP/1.1",200,1584379,"-","Mozilla/5.0 (compatible;Baiduspider/2.0;+http://www.baidu.com/search/spider.html)","-",0.107,-,2019-06-24T17:57:26+08:00,TLSv1.2',
    '220.181.108.81,-,-,[24/Jun/2019:18:23:57,+0800],https,www.domain.com,443,"GET,/thread-168033-1-1.html,HTTP/1.1",200,1753,"-","Mozilla/5.0 (compatible;Baiduspider/2.0;+http://www.baidu.com/search/spider.html)","-",0.064,0.064,2019-06-24T18:23:57+08:00,TLSv1.2',
    '111.206.221.49,-,-,[24/Jun/2019:18:23:57,+0800],https,www.domain.com,443,"GET,/thread-168033-1-1.html,HTTP/1.1",200,47493,"https://www.798wd.com/thread-168033-1-1.html","Mozilla/5.0 (compatible;Baiduspider-render/2.0;+http://www.baidu.com/search/spider.html)","-",0.139,0.138,2019-06-24T18:23:57+08:00,TLSv1.2'
]
baidu=0
for line in web_log:
    print(line)
    if'Baiduspider' in line:
        baidu+=1
        print(baidu)
    print('\n')

urls=[]
for line in web_log:
    line_list=line.split(',')
    url=line_list[9]
    urls.append(url)
print('共抓取{num}个页面'.format(num=len(list(set(urls)))))