#!/usr/bin/python3
from math import sqrt,ceil,floor
n=int(input())
def solve(x,y):
    lis=[1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004]
    for i in lis:
        if i>=x:
            low=i
            break
    else:
        low=lis[-1]        
    for i in lis:
        if i>=y:
            high=i
            break  
    else:
        high=lis[-1]              
    #print (low,high)
    ind1=lis.index(low)
    ind2=lis.index(high)
    count=0
    for i in range(ind1,ind2+1):
        try:
            if x<=lis[i]<=y:
                #print (lis[i],end= " ")
                count+=1
        except:
            continue        
    return count    
for i in range(n):
    x,y=map(int,input().split())
    print ("Case #{0}: {1}".format(i+1,solve(x,y)))
