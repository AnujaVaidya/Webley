import sys
import os
import itertools

dr = sys.argv[1]
print ("Data read from ",dr,"\n")

with open(dr, 'r') as my_file:
    data = my_file.read().split("\n")


arr = list();
i = 0

for item in data:   
    line = item.split(",")
    if line[0] == "Target Price" or line[0] == "Target price":
        target  = line[1]
    else:
        if len(line[0]) > 1 and len(line) > 1:
            arr.append(line[1].lstrip('$'))

arr2 = list();
for z in arr:
    t = z.lstrip()
    arr2.append(t)


    
target2 = target.lstrip()
res = list(map(float, arr2))
target = float(target2.lstrip('$'))
result = [seq for i in range(len(res), 0, -1) for seq in itertools.combinations(res, i) if sum(seq) == target]



for x in result:
    str = list();
    for item in data:
        line = item.split(",")
        if len(line[0]) > 1 and len(line) > 1:
            temp = line[1].lstrip()
            temp3 = float(temp.lstrip('$'))
        if temp3 in x:
            str.append(line[0])
    print("\nThe target for the day is, " ,target,"\nThe combination for the dishes are:")
    o = 1
    if len(str) > 0 :
        for p in str:
            print(p)
            
    else:
            print("There is no combination found of dishes with price total equal to target price")



    

