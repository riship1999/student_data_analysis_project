import requests
import socket
import bs4

# resp = requests.get("https://www.brainyquote.com/quote_of_the_day")
# print(resp)
# s = bs4.BeautifulSoup(resp.text, 'lxml')
# print("s", s)
# data2 = s.find('img', {"class":"p-qotd"})
# print(data2)
# #quote = data2['alt']

resp = requests.get("https://indianexpress.com/section/technology/")
print(resp)
s = bs4.BeautifulSoup(resp.text, 'lxml')

print("s", s)
data2 = s.find('h3', {"class":""})
data3 = data2.find('a').text
print(f" data3 is {data3}")
#print("stype",type(s))
