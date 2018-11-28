from math import *

data = raw_input()
data2=data.split('\n')
Ncases=int(data2.pop(0))
data3=[map(int,data2[i].split()) for i in range(0,Ncases)]



def palin(n):
    temp=str(n)[::-1]
    if temp==str(n):
        return 1
    else:
        return 0

def fairsquare(n):
    if palin(n)==1:
        if palin(int(sqrt(n)))==1:
            return 1
        else:
            return 0
    else:
        return 0

def count(a,b):
    asq=int(ceil(sqrt(a)))
    bsq=int(floor(sqrt(b)))
    vals=[i**2 for i in range(asq,bsq+1)]
    return sum(map(fairsquare,vals))

for i in range(0,Ncases):
    a=data3[i][0]
    b=data3[i][1]
    result=count(a,b)
    print 'Case #{0}: {1}'.format(i+1,result)
