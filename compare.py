# coding: utf-8
import csv
import matplotlib.pyplot as plt
import numpy as np

category_name = ['Retail & recreation', 'Grocery & pharmacy', 'Parks', 'Transit stations', 'Workplace', 'Residential']
category_retail = []
category_grocery = []
category_parks = []
category_transit = []
category_workplace = []
category_residential = []

name_dict = {
    'Tokyo':'東京',
    'Fukui':'福井',
    'Chiba':'千葉',
    'Kanagawa':'神奈川',
    'Miyagi':'宮城',
    'Osaka':'大阪',
    'Saitama':'埼玉',
    'Kyoto':'京都',
    'Fukuoka':'福岡',
    'Ibaraki':'茨城',    
    'Toyama':'富山',
    'Gifu':'岐阜',
    'Aomori':'青森',
    'Gunma':'群馬',
    'Ishikawa':'石川',
    'Okinawa':'沖縄',
    'Tochigi':'栃木',
    'Aichi':'愛知',
    'Oita':'大分',
    'Yamanashi':'山梨',
    'Ehime':'愛媛',
    'Kumamoto':'熊本',
    'Hyogo':'兵庫',
    'Nagano':'長野',
    'Shizuoka':'静岡',
    'Yamagata':'山形',
    'Mie':'三重',
    'Nagasaki':'長崎',
    'Fukushima':'福島',
    'Hiroshima':'広島',
    'Hokkaido':'北海道',
    'Kochi':'高知',
    'Okayama':'岡山',
    'Saga':'佐賀',
    'Shiga':'滋賀',
    'Japan':'日本',
    'Kagawa':'香川',
    'Miyazaki':'宮崎',
    'Tokushima':'徳島',
    'Akita':'秋田',
    'Wakayama':'和歌山',
    'Nara':'奈良',
    'Niigata':'新潟',
    'Iwate':'岩手',
    'Kagoshima':'鹿児島',
    'Yamaguchi':'山口',
    'Tottori':'鳥取',
    'Shimane':'島根'
}

def createRankingBarGraph(title, category, data):
    x = []
    y = []
    labels = []
    for r in data:
        y.append(r[-1])
        x.append(r[0])
        labels.append(r[0])
    fig = plt.figure(figsize=(8.0, 4.0))
    plt.bar(x,y)
    plt.title(title)
    plt.ylabel('Percentage')
    plt.xlabel('City')
    plt.subplots_adjust(left=0.1, right=0.95, bottom=0.3, top=0.85)
    plt.xticks(x,labels,rotation='vertical')
    plt.tick_params(labelsize=8)
    #plt.show()
    plt.savefig('result_images/'+category+'.png')

f = open('2020-04-05_JP_Mobility_Report_en.pdf.tsv', 'r')
reader = csv.reader(f, delimiter="\t")


for r in reader:
    if( r[0] == 'Region'):
        header = r
    if( r[1] == category_name[0] ):
        category_retail.append(r)
        count = 0
        for value in category_retail[-1]:
            if( count >= 2 ):
                category_retail[-1][count] = float(value)
            count = count + 1        
        category_retail[-1].remove(category_name[0])
    if( r[1] == category_name[1]):
        category_grocery.append(r)
        count = 0
        for value in category_grocery[-1]:
            if( count >= 2 ):
                category_grocery[-1][count] = float(value)
            count = count + 1
        category_grocery[-1].remove(category_name[1])
    if( r[1] == category_name[2]):
        category_parks.append(r)
        count = 0
        for value in category_parks[-1]:
            if( count >= 2 ):
                category_parks[-1][count] = float(value)
            count = count + 1
        category_parks[-1].remove(category_name[2])
    if( r[1] == category_name[3]):
        category_transit.append(r)
        count = 0
        for value in category_transit[-1]:
            if( count >= 2 ):
                category_transit[-1][count] = float(value)
            count = count + 1
        category_transit[-1].remove(category_name[3])
    if( r[1] == category_name[4]):
        category_workplace.append(r)
        count = 0
        for value in category_workplace[-1]:
            if( count >= 2 ):
                category_workplace[-1][count] = float(value)
            count = count + 1        
        category_workplace[-1].remove(category_name[4])
    if( r[1] == category_name[5]):
        category_residential.append(r)
        count = 0
        for value in category_residential[-1]:
            if( count >= 2 ):
                category_residential[-1][count] = float(value)
            count = count + 1        
        category_residential[-1].remove(category_name[5])

header.remove('Category')
reader = csv.reader(f, delimiter=":")
sorted_category_retail = sorted(category_retail, key=lambda x : x[-1],reverse=False)
sorted_category_grocery = sorted(category_grocery, key=lambda x : x[-1],reverse=False)
sorted_category_parks = sorted(category_parks, key=lambda x : x[-1],reverse=False)
sorted_category_transit = sorted(category_transit, key=lambda x : x[-1],reverse=False)
sorted_category_workplace = sorted(category_workplace, key=lambda x : x[-1],reverse=False)
sorted_category_residential = sorted(category_residential, key=lambda x : x[-1],reverse=True)


f = open('csvs/retail.csv', "w")
print(*header, file=f, sep=",")
for r in sorted_category_retail:
    r[0] = name_dict[r[0]]   
    print(*r, file=f,sep=",")
f.close();

f = open('csvs/grocery.csv', "w")
print(*header, file=f, sep=",")
for r in sorted_category_grocery:
    r[0] = name_dict[r[0]]    
    print(*r, file=f, sep=',')
f.close();    

f = open('csvs/parks.csv', "w")
print(*header, file=f, sep=",")
for r in sorted_category_parks:
    r[0] = name_dict[r[0]]   
    print(*r, file=f, sep=',')
f.close();    

f = open('csvs/transit.csv', "w")
print(*header, file=f, sep=",")
for r in sorted_category_transit:
    r[0] = name_dict[r[0]]   
    print(*r, file=f, sep=',')
f.close();    

f = open('csvs/workplace.csv', "w")
print(*header, file=f, sep=",")
for r in sorted_category_workplace:
    r[0] = name_dict[r[0]]   
    print(*r, file=f, sep=',')
f.close();    

f = open('csvs/residential.csv', "w")
print(*header, file=f, sep=",")
for r in sorted_category_residential:
    r[0] = name_dict[r[0]]   
    print(*r, file=f, sep=',')
f.close();    


#y = sorted_category_retail[0][1:-1]
#labels = header[1:-1]

#flg, ax = plt.subplots()
array_data = []
array_data.append(sorted_category_retail)
array_data.append(sorted_category_grocery)
array_data.append(sorted_category_parks)
array_data.append(sorted_category_transit)
array_data.append(sorted_category_workplace)
array_data.append(sorted_category_residential)

for i in range(len(category_name)):
    createRankingBarGraph(category_name[i] + '['+ str(header[-1]) +']', category_name[i], array_data[i])

