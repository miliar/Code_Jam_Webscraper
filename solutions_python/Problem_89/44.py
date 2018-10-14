from math import *
from itertools import *
from fractions import *

#name = "C-large"
name = "C-small-attempt0"
f_in = open(name + '.in',"r")
f_out = open(name + '.out','w')

def addN(N,p):
        t = p**2
        ret = []
        while (t <= N):
                ret.append(t)
                t = t*p
        return ret
        
def  primes(N):
        pr = []
        for x in range(2,N):
                ret = True
                for y in pr:
                        if(x%y == 0):
                                ret = False
                                break
                if(ret):
                        pr.append(x)
        return pr
B = 400
pr = primes(B)
print(len(pr))
ar = []
for x in pr:
        if(x <= B):
                ar = ar + addN(B**2,x)

print(len(ar))
ar.sort()
print("lala")
T  =  int(f_in.readline())    
for i in range(T):
        print("i",i)
        N  =  int(f_in.readline())
        
        ret = 1
        if(N == 1):
                f_out.write("Case #" +str(i+1) + ": " +str(0)+"\n")
        else:
                ret = 1
                while(ar[ret - 1] <= N):
                        ret = ret + 1
                f_out.write("Case #" +str(i+1) + ": " +str(ret)+"\n")
                              
f_in.close()
f_out.close()
