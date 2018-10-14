from random import *

def roundout(lst,no,c):
    if lst[no] == ['?']*c:
        if lst[no+1]==['?']*c:
            roundout(l,no+1,c)
        else:
            for we in range(no+1):
                lst[we] = lst[no+1]
def randomizer(l,r,c):
    lst = list(l)
    d=[]
    for m in range(r):
        d = []
        i=-1
        j =-1
        for n in lst[m]:
            if n!='?' and n not in d:
                d.append(n)
        for n in range(c):
            if lst[m][n]!='?':
                i = m
                j =n
                
            elif lst[m][n]=='?':
                if i>=0:
                    lst[m][n] = lst[i][j]
                else:
                    if len(d)!=0:
                        lst[m][n]= d[0]
                    elif m>0:
                       lst[m]=lst[m-1]
    for m in range(r):
        if lst[m]==['?']*c:            
            roundout(lst,m,c)
            
    return lst



n = int(input())
for  i in range(n):
    r,c = (int(p) for p in input().split())
    l= []
    d=[]
    for j in range(r):
        a =(input())
        l.append(list(a))

    lst1 = randomizer(l,r,c)



    print("Case #"+str(i+1)+":")
    for q in range(r):
        r1 = ''
        for w in range(c):
            r1+=lst1[q][w]
        print(r1)
        
