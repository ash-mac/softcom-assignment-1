import requests
import os
from bs4 import BeautifulSoup
import pprint
import sys
import textwrap

#################################################################################################

if not os.path.exists('India'):
    os.mkdir('India')


ind = requests.get('https://timesofindia.indiatimes.com/india')
soup1 = BeautifulSoup(ind.text,"html.parser")
links1 = soup1.select('.w_tle')


list_links1 = []
for i in range(len(links1)):
    for atag in links1[i].find_all('a'):
        list_links1.append(atag.get('href'))



l1=[]
for idx,item in enumerate(links1):
    title = links1[idx].getText()
    l1.append(title)
list_titles = l1


reslist = []
for i in range(len(links1)):
    url = list_links1[i]
    if 'timesofindia.indiatimes.com' not in url:
        url='http://timesofindia.indiatimes.com'+url[:]
    reslist.append(url)


dates = []
text_content = []
for i in range(len(reslist)):
    if(i<len(reslist)):
        url = reslist[i]
        try:
            temp = requests.get(url)
        except:
            requests.exceptions
        souptemp = BeautifulSoup(temp.text,"html.parser")
        tempdate = souptemp.select('._3R_Dd')
        if(len(tempdate)):
            dates.append(tempdate[0].getText())
        else:
            dates.append(None)
        texttemp = souptemp.select('.ga-headlines')
        if(len(texttemp)):
            text_content.append(texttemp[0].getText())
        else:
            text_content.append(None)


orig_stdout = sys.stdout
f1 = open('India\out1.txt', 'w',encoding = 'utf-8')
sys.stdout = f1
for i in range(len(reslist)):
    if(i<len(list_titles) and i<len(reslist) and i<len(dates) and i<len(text_content)):
        print('Title\n',list_titles[i],'\n')
        print('Link\n',reslist[i],'\n')
        print('Date and Time\n',dates[i],'\n')
        print('Text\n',text_content[i],'\n')
sys.stdout = orig_stdout
f1.close()


########################################################################################

if not os.path.exists('World'):
    os.mkdir('World')


ind = requests.get('https://timesofindia.indiatimes.com/world')
soup1 = BeautifulSoup(ind.text,"html.parser")
links1 = soup1.select('.w_tle')


list_links1 = []
for i in range(len(links1)):
    for atag in links1[i].find_all('a'):
        list_links1.append(atag.get('href'))



l1=[]
for idx,item in enumerate(links1):
    title = links1[idx].getText()
    l1.append(title)
list_titles = l1


reslist = []
for i in range(len(links1)):
    url = list_links1[i]
    if 'timesofindia.indiatimes.com' not in url:
        url='http://timesofindia.indiatimes.com'+url[:]
    reslist.append(url)


dates = []
text_content = []
for i in range(len(reslist)):
    if(i<len(reslist)):
        url = reslist[i]
        try:
            temp = requests.get(url)
        except:
            requests.exceptions
        souptemp = BeautifulSoup(temp.text,"html.parser")
        tempdate = souptemp.select('._3R_Dd')
        if(len(tempdate)):
            dates.append(tempdate[0].getText())
        else:
            dates.append(None)
        texttemp = souptemp.select('.ga-headlines')
        if(len(texttemp)):
            text_content.append(texttemp[0].getText())
        else:
            text_content.append(None)


orig_stdout = sys.stdout
f1 = open('World\out2.txt', 'w',encoding = 'utf-8')
sys.stdout = f1
for i in range(len(reslist)):
    if(i<len(list_titles) and i<len(reslist) and i<len(dates) and i<len(text_content)):
        print('Title\n',list_titles[i],'\n')
        print('Link\n',reslist[i],'\n')
        print('Date and Time\n',dates[i],'\n')
        print('Text\n',text_content[i],'\n')
sys.stdout = orig_stdout
f1.close()


########################################################################################

if not os.path.exists('Business'):
    os.mkdir('Business')


ind = requests.get('https://timesofindia.indiatimes.com/business')
soup1 = BeautifulSoup(ind.text,"html.parser")
links1 = soup1.select('.w_tle')


list_links1 = []
for i in range(len(links1)):
    for atag in links1[i].find_all('a'):
        list_links1.append(atag.get('href'))



l1=[]
for idx,item in enumerate(links1):
    title = links1[idx].getText()
    l1.append(title)
list_titles = l1


reslist = []
for i in range(len(links1)):
    url = list_links1[i]
    if 'timesofindia.indiatimes.com' not in url:
        url='http://timesofindia.indiatimes.com'+url[:]
    reslist.append(url)


dates = []
text_content = []
for i in range(len(reslist)):
    if(i<len(reslist)):
        url = reslist[i]
        try:
            temp = requests.get(url)
        except:
            requests.exceptions
        souptemp = BeautifulSoup(temp.text,"html.parser")
        tempdate = souptemp.select('._3R_Dd')
        if(len(tempdate)):
            dates.append(tempdate[0].getText())
        else:
            dates.append(None)
        texttemp = souptemp.select('.ga-headlines')
        if(len(texttemp)):
            text_content.append(texttemp[0].getText())
        else:
            text_content.append(None)


orig_stdout = sys.stdout
f1 = open('Business\out3.txt', 'w',encoding = 'utf-8')
sys.stdout = f1
for i in range(len(reslist)):
    if(i<len(list_titles) and i<len(reslist) and i<len(dates) and i<len(text_content)):
        print('Title\n',list_titles[i],'\n')
        print('Link\n',reslist[i],'\n')
        print('Date and Time\n',dates[i],'\n')
        print('Text\n',text_content[i],'\n')
sys.stdout = orig_stdout
f1.close()


########################################################################################


if not os.path.exists('Homepage'):
    os.mkdir('Homepage')


ind = requests.get('https://timesofindia.indiatimes.com/')
soup1 = BeautifulSoup(ind.text,"html.parser")
links1 = soup1.select('.list8')

list_links1 = []
a_mega_list=[]
a_tag_list = []
for i in range(len(links1)):
    a_mega_list.append(links1[i].find_all('a'))
for a_list in a_mega_list:
    for atag in a_list:
        a_tag_list.append(atag)
        list_links1.append(atag.get('href'))
# pprint.pprint(list_links1)

l1=[]
for idx,item in enumerate(a_tag_list):
    title = a_tag_list[idx].getText()
    l1.append(title)
list_titles = l1

# pprint.pprint(a_list[0])
reslist = []
for i in range(len(a_tag_list)):
    url = list_links1[i]
    if 'timesofindia.indiatimes.com' not in url:
        url='http://timesofindia.indiatimes.com'+url[:]
    reslist.append(url)


dates = []
text_content = []
for i in range(len(reslist)):
    url = reslist[i]
    try:
        temp = requests.get(url)
    except:
        requests.exceptions
    souptemp = BeautifulSoup(temp.text,"html.parser")
    tempdate = souptemp.select('._3R_Dd')
    # tempdate = pretempdate[0].find('span')
    if(len(tempdate)):
        dates.append(tempdate[0].getText())
    else:
        dates.append(None)
    texttemp = souptemp.select('.ga-headlines')
    if(len(texttemp)):
        text_content.append(texttemp[0].getText())
    else:
        text_content.append(None)


orig_stdout = sys.stdout
f1 = open('Homepage\out4.txt', 'w',encoding = 'utf-8')
sys.stdout = f1
for i in range(len(reslist)):
    if(i<len(list_titles) and i<len(reslist) and i<len(dates) and i<len(text_content)):
        print('Title\n',list_titles[i],'\n')
        print('Link\n',reslist[i],'\n')
        print('Date and Time\n',dates[i],'\n')
        print('Text\n',text_content[i],'\n')
sys.stdout = orig_stdout
f1.close()


########################################################################################

