from bs4 import BeautifulSoup
import requests
import json, csv
import random
from time import sleep


headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/94.0.4606.81 Safari/537.36'
}
# companies_url_list = {}

# for i in range(65):
#     print(f"Итерация №{i}")
#     req = requests.get(url=f'https://clutch.co/it-services/analytics?page={i}', headers=headers)
#     src = req.text
#     soup = BeautifulSoup(src, 'lxml')
#     blocks_copmany = soup.find_all('h3')
#     companies_info = []
#     for item in blocks_copmany:
#         companies_info.append(item.find('a'))
#     for item in companies_info:
#         try:
#             end = item.get('href')
#             full_url = 'https://clutch.co/' + end
#             text = item.text.strip("\n ")
#             companies_url_list[text] = full_url
#         except:
#             pass
# with open('all_companies_url.json', 'w', encoding='utf-8') as file:
#     json.dump(companies_url_list, file, indent=1, ensure_ascii=False)
#
# print(len(companies_url_list))

# with open('index.html', 'w', encoding='utf-8') as file:
#     file.write(src)

# with open('index.html', encoding='utf-8') as file:
#     page = file.read()

# soup = BeautifulSoup(page, 'lxml')
#
# blocks_copmany = soup.find_all('h3')
#
# companies_info = []
# for item in blocks_copmany:
#     companies_info.append(item.find('a'))
# print(companies_info)

with open('result.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(
        ('name', 'description', 'phone', 'web', 'min_project_size')
    )
    file.close()



with open('all_companies_url.json', encoding='utf-8') as file:
    companies_list = json.load(file)
it_company = {}
count = 0

proxies = {
    'https':'198.144.149.82:3128',
}

for item in companies_list:
    print(f'Количество итераций: {count}')
    try:
        page = requests.get(companies_list[item], headers=headers).text
        soup = BeautifulSoup(page, 'lxml')
        name = soup.find('a', class_='website-link__item').text.strip(' \n')
        print(name)
        description = soup.find('p').text
        phone = soup.find('a', class_="contact phone_icon").text.strip(' \n')
        web = soup.find('a', class_='web_icon website-link__item').get('href').split('/?')[0]
        min_project_size = soup.find('div', class_='list-item custom_popover').find('span').text
        with open('result.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow((name, description, phone, web, min_project_size))
        count += 1
        sleep(random.randrange(5, 10))
    except:
        count +=1


















