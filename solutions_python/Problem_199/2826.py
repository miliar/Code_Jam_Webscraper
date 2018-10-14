'''
Created on Apr 7, 2017

@author: TigerZhao
'''

f=open("A-large (1).in","r")

T=int(f.readline())

def flip(p,start,end):
    for i in range(start, end):
        if p[i]=="-":
            p[i]="+"
        else:
            p[i]="-"
    

def getAns(p,s):
    flips=0
    tmp=[]
    for i in range(len(p)-s+1):
        if p[i] =="-":
            flip(p,i,i+s)
            flips+=1
    if "-" in p:
        return "IMPOSSIBLE"
    return flips

for i in range(1,T+1):
    p,s=f.readline().split()
    s=int(s)
    p=list(p)
    print "Case #{0}: {1}".format(i,getAns(p,s))
    


f.close()
