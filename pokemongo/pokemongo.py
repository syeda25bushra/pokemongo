import csv
  
from itertools import combinations
# csv file name
filename = "poke.csv"
  
# initializing the titles and rows list
fields = []
rows = []
rowlist=[]
rowlist.sort(key=None, reverse=False)
# print(type(rowlist))
# print(type(rowlist)==list)
# reading csv file
def ss(a,c):
    b=[]
    for i in a:
        k=[str(j) for j in i]
        k=list(set(k))
        k.sort()
        b.append(k)
        pass
    l=[str(j) for j in c]
    l=list(set(l))
    l.sort()
    return l in b
    pass
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
    
comb = combinations(rows[1:], 3)
greeater={}
leseser={}
noremal={}
for i in list(comb):
    row=[]
    a,b,c=i 
    greater_one_count=0
    one_count=0
    less_one_count=0
    for tup in i:
        row.append(tup[0])
        row.append(tup[1])
#             print(tup[0].split()[0])
#             row.append(tup[1])
    count=0   
    for count in range(2,len(a)-1):
        row.append(max(a[count],b[count],c[count]))
#             count=count+1
    for count in range(6,len(row)-1):
        if(float(row[count])>1):
            greater_one_count=greater_one_count+1
        if(float(row[count])<=1):
            one_count=one_count+1
        if(float(row[count])<1):
            less_one_count=less_one_count+1
    if(len(greeater)>9):
        if(greater_one_count in greeater.keys()):
            if(type(greeater[greater_one_count])==list and type(greeater[greater_one_count][0])==list):
                
                greeater[greater_one_count].sort(key=lambda x : int(x[-1]), reverse=False)
                if(int(greeater[greater_one_count][-1][-1]) > less_one_count):
                    del greeater[greater_one_count][-1]
                    greeater[greater_one_count].append(row[:6]+[less_one_count])
                elif (len(greeater[greater_one_count])<10):
                    lk=row[:6]+[less_one_count]
                    if(not ss(greeater[greater_one_count].copy(),lk.copy())):
                        greeater[greater_one_count].append(row[:6]+[less_one_count])
                   
            else:
                greeater[greater_one_count]=[greeater[greater_one_count],row[:6]+[less_one_count]]
            pass
        elif (greater_one_count>min(greeater.keys())):
            del greeater[min(greeater.keys())]
            greeater[greater_one_count]=row[:6]+[less_one_count]
            pass
    else:
        if(greater_one_count in greeater.keys()):
            if(type(greeater[greater_one_count])==list and type(greeater[greater_one_count][0])==list):
                
                greeater[greater_one_count].sort(key=lambda x : int(x[-1]), reverse=False)
                if(int(greeater[greater_one_count][-1][-1]) > less_one_count):
                    del greeater[greater_one_count][-1]
                    greeater[greater_one_count].append(row[:6]+[less_one_count])
                elif (len(greeater[greater_one_count])<10):
                    lk=row[:6]+[less_one_count]
                    if(not ss(greeater[greater_one_count].copy(),lk.copy())):
                        greeater[greater_one_count].append(row[:6]+[less_one_count])
                  
            else:
                greeater[greater_one_count]=[greeater[greater_one_count],row[:6]+[less_one_count]]
                
            pass
        else:
            greeater[greater_one_count]=row[:6]+[less_one_count]
#     if(len(leseser)>9):
#         if(less_one_count in leseser.keys()):
#             if(type(leseser[less_one_count])==list and type(leseser[less_one_count][0])==list):
#                 leseser[less_one_count].append(row[:6])
#             else:
#                 leseser[less_one_count]=[leseser[less_one_count],row[:6]]
#                 
#             pass
#         elif (less_one_count<min(leseser.keys())):
#             del leseser[max(leseser.keys())]
#             leseser[less_one_count]=row[:6]
#             pass
#     else:
#         if(less_one_count in leseser.keys()):
#             if(type(leseser[less_one_count])==list and type(leseser[less_one_count][0])==list):
#                 leseser[less_one_count].append(row[:6])
#             else:
#                 leseser[less_one_count]=[leseser[less_one_count],row[:6]]
#                 
#             pass
#         else:
#             leseser[less_one_count]=row[:6]
#     rowlist.append(row)  

print(greeater)
print(max(greeater.keys()))
print(greeater[max(greeater.keys())])
# print(leseser)

     

#         rowlist=rowlist.append()
#         print (i)
  
    # extracting each data row one by one
#     for row in csvreader:
#         rows.append(row)
  
    # get total number of rows
#     print("Total no. of rows: %d"%(csvreader.line_num))
  
# printing the field names
# print('Field names are:' + ', '.join(field for field in fields))

