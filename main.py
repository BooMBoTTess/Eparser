import requests as r
import re
RESTAB_POSITION = 3

with open('page.html', 'r', encoding='UTF-8') as f:
    res = f.read()

# card = re.findall('<tr valign=middle bgcolor=#f5f5f5.*</tr>', res)
all_pages = re.findall('С\. \S*', res)
all_titles = re.findall('<span style="line-height:1.0;">.*</span>', res)
all_names = re.findall('<i>.*</i>', res)
all_datas = re.findall('20\d\d\.', res)
all_numbers_docs = re.findall('№&nbsp;.*</a>', res)
all_journals = re.findall('<a href="/contents.*</a>.', res)
all_journals = [all_journals[i] for i in range(0, len(all_journals), 2)]
print(len(all_pages), len(all_titles), len(all_names), len(all_datas), len(all_numbers_docs), len(all_journals))

all_pages = all_pages
all_datas = all_datas
all_names = [re.findall('>.*<', el)[0].strip('>').strip('<')  for el in all_names]
all_numbers_docs = [el.replace('&nbsp;', ' ').replace('</a>', '')  for el in all_numbers_docs]
all_titles = [el[el.find('>')+1 : el.find('</span')]  for el in all_titles]
all_journals = [el[el.find('>')+1 : el.find('</a')]  for el in all_journals]

with open('list_literature.txt', 'a') as f:
    for i in range(100):
        result = f'{all_names[i]} {all_titles[i]} // {all_journals[i]} - {all_datas[i]} - {all_numbers_docs[i]} - {all_pages[i]}'
        print(result)
        print(result, file=f)

