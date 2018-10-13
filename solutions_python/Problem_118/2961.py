from math import *
import string

def isP(d):
    s=str(d)
    flag=True
    for i in range(len(s)/2):
        if s[i]!=s[-i-1]:
            flag=False
    return flag

def solve(a,b):
    k=0
    for i in range(a,b+1):
        if int(sqrt(i))**2==i and isP(i) and isP(int(sqrt(i))):
            k+=1
    return k
    
out=''
ss=raw_input()
ss=string.split(ss,'\n')

T=int(ss[0])
f =open('D:\out.txt','w')
for i in range(1,T+1):
    (a,b)=map(int,string.split(ss[i],' '))
    s= 'Case #'+str(i)+': '+str(solve(a,b))+'\n'
    f.write(s)

f.close()
    
    
