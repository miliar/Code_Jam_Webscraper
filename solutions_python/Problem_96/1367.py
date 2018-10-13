'''
Created on 2012-4-14

@author: Matrix
'''
import sys,cmath
#sys.stdin=open("B-large.in","r")
#sys.stdout=open("out.txt","w")
t=int(raw_input())
for i in xrange(t):
    data=map(int,raw_input().split())
    n=data[0];s=data[1];p=data[2]
    ans=0;num1=0;num2=0;num3=0
    for d in data[3:]:
        if d%3==0:
            if d/3>=p : ans+=1
            elif d/3>=p-1 and d!=0: num1+=1
        elif d%3==1:
            if d/3>=p or d/3>=p-1 : ans+=1
        elif d%3==2:
            if d/3>=p or d/3>=p-1 : ans+=1
            elif d/3>=p-2 : num3+=1
    print "Case #%d: %d" % (i+1,ans+min(num3+num1,s))