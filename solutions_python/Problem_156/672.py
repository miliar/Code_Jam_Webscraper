from math import log,ceil,floor
from copy import deepcopy
def getToN(dishList,n):
    sum = 0
    for i in dishList:
        if i > n:
            sum += (i-1)//n
    return sum
def fori(dishList,maxi):
    result = []
    if maxi == 1:
        return 1
    for i in range(1,maxi):
        #tempList = deepcopy(dishList)
        tempSum = getToN(dishList,i)
        result.append(tempSum+i)
    return min(min(result),maxi)
def solve(dishCount , dishList,firstBest, step):
    biggest = dishList[0]
    if step+floor(log(biggest, 2)) > firstBest:
        return biggest
    dishList.pop(0)
    dishList.append(biggest//2)
    dishList.append(biggest//2 + (biggest - (2*(biggest//2))))
    dishList.sort(reverse=True)
    newBiggest  = solve(dishCount+1, dishList,firstBest,step+1)
    if newBiggest+1 >= biggest:
        return biggest
    else:
        return 1 + newBiggest
FILE = open("test.txt", 'r')
output = open("result.txt",'w')
Testnumber = int(FILE.readline())
print("reading", Testnumber, "test")
for i in range (0,Testnumber):
    dishNumber = int(FILE.readline())
    dishString = FILE.readline()
    dishList = dishString.split(" ")
    dishList = [int(x) for x in dishList]
    dishList.sort(reverse=True)
    print("list of dishes", dishList, "---",str(i))
    # print("FOOORI", fori(dishList,max(dishList)))
    output.write('Case #'+str(i+1)+': '+str(fori(dishList,max(dishList)))+'\n')
