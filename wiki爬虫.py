from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql.cursors

resp = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")
soup = BeautifulSoup(resp, "html.parser")
listUrls = soup.findAll("a", href=re.compile("^/wiki/"))
for url in listUrls:
	if not re.search("\.(jpg|JPG)$", url["href"]):
		print(url.get_text(), "<---->", "http://en.wikipedia.org" + url["href"])
		connection = pymysql.connect(host='localhost',
		                             user='root',
		                             password='123456',
		                             db='main',
		                             charset='utf8mb4')
		try:
			with connection.cursor()as cursor:
				sql = "insert into `wiki_search_article`(`title`,`content`) values (%s,%s)"
				
				cursor.execute(sql, (url.get_text(), "http://en.wikipedia.org" + url["href"]))
				
				connection.commit()
		finally:
			connection.close()