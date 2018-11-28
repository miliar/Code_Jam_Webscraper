from sys import argv,exit
import itertools
from math import ceil

def bad_sum(pile):
    binary =[]       
    for sweet in pile:
        binary.append( bin(sweet)[2:] ) 
    total = ''
    for n in binary:
        total = bad_add(total,n)
    return total
    
def bad_add(a,b):
    L = max(len(a), len(b))
    a,b = a.zfill(L), b.zfill(L) 
    T = ''
    for i in xrange(L):
        j = L-1-i
        if a[j] == b[j]:
            T = '0' + T
        else:
             T = '1' + T
    return T    

f = open( argv[1] )
for i in xrange(int(f.readline())):
    f.readline()
    candy = [int(a) for a in f.readline().split()]
    piles = []
    for a in xrange((len(candy)-1)/2,len(candy)-1):
        piles += list(itertools.combinations(candy,a+1))
    piles = sorted(piles,key=sum)
    piles.reverse()
    
    test = True
    b = 0
    while b < len(piles) and test:
        pile1 = piles[b]
        b += 1
 
        pile2 = candy[:]
        for sweet in pile1:
            pile2.remove(sweet)
        
        sum1,sum2 = bad_sum(pile1),bad_sum(pile2)
        L = max(len(sum1), len(sum2))
        sum1,sum2 = sum1.zfill(L),sum2.zfill(L) 
        if sum1 == sum2:
            test = False
            
    if not test:
        R = str(sum(pile1))
    else:
        R = 'NO'
        
    print "Case #"+str(i+1)+": "+R
f.close()
