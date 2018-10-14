from copy import *
from math import *

fi=open("D.in")

#f=open("bound.txt")

def I():
    s=fi.readline()
    s=s.strip()
    s=int(s)
    return s

def S():
    s=fi.readline()
    s=s.strip();
    return s

def read():
    s=S()
    s=s.split()
    for i in [0,1,2]:
        s[i]=int(s[i])
    return s
def permutate(seq):
    """permutate a sequence and return a list of the permutations"""
    if not seq:
        return [seq]  # is an empty sequence
    else:
        temp = []
        for k in range(len(seq)):
            part = seq[:k] + seq[k+1:]
            #print k, part  # test
            for m in permutate(part):
                temp.append(seq[k:k+1] + m)
                #print m, seq[k:k+1], temp  # test
        return temp



noTest=I()

for at in range(noTest):
    n=I()
    s=S()
    t=""
    for i in range(n):
        t+=str(i+1)
    L=permutate(t)
    l=len(s)
    mi=10000000000000000
    for i in L:
        count=0
        last="A"
        
        for j in range(0,l,n):
            for k in range(j,j+n):
                if s[j+ int(i[j-k]) -1] != last:
                    count+=1
                    last = s[j+ int(i[j-k]) -1]
        if mi > count :
            mi = count
    #print mi,at+1
    print "Case #%d: %d" %(at+1,mi)
    
            
        
        
        
        



# a simple recursive permutation function
# the number of permutations of a sequence of n unique items is given by n! (n factorial)
# more details at http://mathworld.wolfram.com/Permutation.html
# tested with Python24      vegaseat      16feb2006













    
    
