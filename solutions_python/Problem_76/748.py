import re
from operator import add

def PatrickAdd(pile = []):
    total = '0'
    for candy in pile:
        val = bin(int(candy))
        total = str( int(val[2:]) + int(total) )
        total = total.replace('2', '0')
    return int(total,2)
    
def SeanAdd(pile = []):
    total = 0
    for candy in pile:
        total += int(candy)
    return total
    
def findMin(list = []):
    minindex = -1
    min = 999999999
    for i in range(len(list)):
        if int(list[i]) < min:
            min = int(list[i])
            minindex = i
    return minindex
        
i = open('C-large.in', 'r')
o = open('C-large.out', 'w')

T = int(i.readline())

for j in range(T):
    N = i.readline()
    pile = i.readline()
    pile = re.split('\s+', pile)
    if pile[len(pile)-1] == '':
        pile.remove('')
    Spile = pile
    Ppile = []
    splitfound = False
    
    while Spile != []:
        Sval = PatrickAdd(Spile)
        Pval = PatrickAdd(Ppile)
        if Sval == Pval and Sval != 0:
            splitfound = True
            break     
        Ppile.append(Spile[findMin(Spile)])
        Spile.remove(Spile[findMin(Spile)])
        
    if splitfound:
        o.write('Case #'+str(j+1)+': '+str(SeanAdd(Spile))+'\n')
    else:
        o.write('Case #'+str(j+1)+': NO\n')
i.close()
o.close()
