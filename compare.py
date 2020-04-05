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

f = open('2020-03-29_JP_Mobility_Report_en.pdf.tsv', 'r')
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

f = open('tsvs/retail.tsv', "w")
for r in sorted_category_retail:
    print(r, file=f)
f.close();

f = open('tsvs/grocery.tsv', "w")
for r in sorted_category_grocery:
    print(r, file=f)
f.close();    

f = open('tsvs/parks.tsv', "w")
for r in sorted_category_parks:
    print(r, file=f)
f.close();    

f = open('tsvs/transit.tsv', "w")
for r in sorted_category_transit:
    print(r, file=f)
f.close();    

f = open('tsvs/workplace.tsv', "w")
for r in sorted_category_workplace:
    print(r, file=f)
f.close();    

f = open('tsvs/residential.tsv', "w")
for r in sorted_category_residential:
    print(r, file=f)
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

