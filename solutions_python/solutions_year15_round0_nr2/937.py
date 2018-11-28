import math

def cut(panArr, cutParts):
    maxi = max(panArr)
    partSize = int(maxi/cutParts)
    rest = maxi%cutParts
    index = panArr.index(max(panArr))
    panArr[index] = partSize
    for i in range(1,cutParts):
        if rest != 0:
            panArr.append(partSize+1)
            rest-=1
        else:
            panArr.append(partSize)
    return panArr,cutParts-1

def bruteFinder(panArr, special):
    time = max(panArr)
    first = time
    special = 0
    cost=1
    while(cost!=0):
        panArr, cost = cut(panArr)
        special+=cost
        if special + max(panArr) < time:
            time = special + max(panArr)
        if special > first:
            break
    return time

def bruteFind(panArr, special = 0):
    maxi = max(panArr)
    time = max(panArr) + special
    #if special > 10:
     #   return time
    for cutParts in range(2,int(math.sqrt(maxi))+1):
        newArr, cost = cut(panArr[:],cutParts)
        if cost == 0 :
            continue
        time = min([bruteFind(newArr,special + cost),time])
    return time


file = open("B-small-attempt3.in")
lines = file.read().split("\n")
out = open("output", 'w')
for case in range(1,int(lines[0])+1):
    if case!=1:
        out.write("\n")
    line = lines[case * 2]
    line = line.split(" ")
    panArr = [int(i) for i in line]
    time = bruteFind(panArr)
    print("Case #" + str(case) + ": " + str(time))
    out.write("Case #" + str(case) + ": " + str(time))
out.close()
