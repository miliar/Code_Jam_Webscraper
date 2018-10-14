#!/bin/python



##
def is_palin(X):
    
    Y = int("".join(reversed(str(X))))
    return X==Y
    

##
import math
def number_fairs(A,B):
    cpt=0
    for i in xrange(A,B+1):
        racine = math.sqrt(i)
        if racine - math.floor(racine) == 0:
            if is_palin(int(racine)):
                if is_palin(i):
                    cpt+=1;
    return cpt
            

#prepare input
"""
f=open("in2","w")
import random

rand=random.randint
f.write("100\n")
for k in xrange(100):
    f.write("100 100\n")
    for i in xrange(100):
        s=[]
        for j in xrange(100):
            s.append(str(rand(1,100)))
        f.write(" ".join(s))
        f.write("\n")
"""



# read the input
f=open("in")
T=int(f.readline())


output=""
for i in xrange(T):
    raw_list=map(lambda x:int(x),f.readline()[:-1].split())
    A,B=raw_list[0],raw_list[1]
    print i
    output+="Case #%d: %s\n" % (i+1,number_fairs(A,B))
    
    
    
    
OUTPUT=open("out","w")
OUTPUT.write(output)
print output
print "done"



    
    
    
