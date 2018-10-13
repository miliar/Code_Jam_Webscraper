'''
Created on Apr 8, 2017

@author: TigerZhao
'''
'''
Created on Apr 7, 2017

@author: TigerZhao
'''

f=open("B-large.in","r")

T=int(f.readline())

def nines(n, start):
    for i in range(start, len(n)):
        n[i]=9

def getAns(n):
    n=[int(x) for x in list(str(n))]

    for i in range(len(n)):
        for x in range(len(n)-1):
            if n[x]>n[x+1]:
                n[x]-=1
                nines(n,x+1)
    n=[str(x)for x in n]
    return int("".join(n).strip())
                
        
for i in range(1,T+1):
    n=int(f.readline())
    print "Case #{0}: {1}".format(i,getAns(n))
    


f.close()
