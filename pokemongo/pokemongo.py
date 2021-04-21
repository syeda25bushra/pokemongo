import csv
  
from itertools import combinations
from django.db.models.aggregates import Count
# csv file name
filename = "poke.csv"
  
# initializing the titles and rows list
fields = []
rows = []
  
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        r1=[]
        for column in row[0].split():
            r1.append(column)
        rows.append(r1)
#         print("\n")
#     # extracting field names through first r zow
#     fields = next(csvreader)
    rowlist=[]
    comb = combinations(rows[1:], 3)
    for i in list(comb):
        row=[]
        a,b,c=i 
        for tup in i:
            row.append(tup[0])
            row.append(tup[1])
#             print(tup[0].split()[0])
#             row.append(tup[1])
        count=0   
        for count in range(2,len(a)-1):
            row.append(max(a[count],b[count],c[count]))
#             count=count+1
        
        rowlist.append(row)            
    with open("out.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rowlist)
#         rowlist=rowlist.append()
#         print (i)
  
    # extracting each data row one by one
#     for row in csvreader:
#         rows.append(row)
  
    # get total number of rows
#     print("Total no. of rows: %d"%(csvreader.line_num))
  
# printing the field names
# print('Field names are:' + ', '.join(field for field in fields))

