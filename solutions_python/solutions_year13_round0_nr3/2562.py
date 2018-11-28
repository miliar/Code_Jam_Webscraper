import sys

from math import *

def sq(x):
    return x*x
andpals=[]

def lennro(x):
    if x==0: return 1
    return int(ceil(log10(x)))
pals=[]
cumpletodo=[]
todos=[]
def makepal(length):
    todos=[]
    todosi=[]
    for i in range(1,10):
        todosi.append(i*10+i)
    latests=range(10)    
    todos=range(10)
    latestsi=todosi
    for i in range(2,length):
        new=[]
        newi=[]
        for e in latests:
            for j in range(1,10):
                x=j*10**(lennro(e)+1)+e*10+j                
                new.append(x)
        for e in latestsi:
            for j in range(1,10):
                x=j*10**(lennro(e)+1)+e*10+j
                newi.append(x)
        latests = new
        todos = todos + latests
        latestsi=newi
        todosi = todosi + latestsi
    
    return sorted(todos + todosi)[1:]
def intsqrt(x):
    return int(floor(sqrt(x)))
def issq(x):
    b=intsqrt(x)
    return b**2==x

def preload():
    lpals= sorted(makepal(7))
    pals =  set(lpals)
    for i in lpals:
        sq=i*i
        if(sq in pals):
            cumpletodo.append(sq)
    return 

def solve(a,b):
    i=0
    validos = [i for i in cumpletodo if a<=i<=b]

    return len(validos)

def main():
   l = sys.stdin.readlines()
   n = int(l[0])
   preload()
    
   for x,i in enumerate(l[1:]):
       a,b = map(int,i.split(' '))
       print "Case #"+str(x+1)+": " +str(solve(a,b))
   return 



if __name__=='__main__':
    main()
