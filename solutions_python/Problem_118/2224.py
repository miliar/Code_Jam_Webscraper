#2.03
from math import sqrt

def square(num):
    return (sqrt(num) == int(sqrt(num)))    

def fair(num):
    s = str(num)
    par = 0
    
    for i in range(0, (len(s)/2)):
        if(s[i] == s[len(s)-i-1]):
            par = par + 1

    if(par == (len(s)/2)):
        return True
    else:
        return False
    
def numOfSquareAndFair(start, end):
    count = 0
    for i in range(start, (end+1)):
        if (fair(i) & square(i)):
            if( fair(int(sqrt(i))) ):
                count = count + 1
    return count

#----------------------------------------------------

f = open("C-small-attempt1.in","r")
x = f.readline()
x = x.split()
N  = int(x[0])


rangeList = []
for i in range(0,N):
    temp = []
    x = f.readline()
    x = x.split()
    temp.append(int(x[0]))
    temp.append(int(x[1]))
    rangeList.append(temp)

for i in range(0,N):
    s = "Case #" + str(i+1) + ":"
    print s, numOfSquareAndFair(rangeList[i][0],rangeList[i][1])

