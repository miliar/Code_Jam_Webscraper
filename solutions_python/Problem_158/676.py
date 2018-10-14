'''
Created on 12/04/2014

@author: david
'''

#f=open("exampleD.txt")
f=open("D-small-attempt2.in")
#f=open("D-large.in")

T=int(f.readline())
P=[]
for i in range(T):
    x,r,c = [int(n) for n in f.readline().split()]
    P.append((x,r,c))

def solve(x,r,c):
    if x==1: return "GABRIEL"
    if x>=7: return "RICHARD"
    if ((r*c) % x) != 0: return "RICHARD"
    if x==2: return "GABRIEL"
    ma = max(r,c)
    mi = min(r,c)
    if x==4:
        if mi==2 and ma==4: 
            return "RICHARD"
    if ma<x: return "RICHARD"
    #if x-mi >= mi+1: return "RICHARD"
    #"""
    x1 = x//2
    x2 = x-x1
    xa_mi = min(x1+1,x2)
    xa_ma = max(x1+1,x2)
    xb_mi = min(x1,x2+1)
    xb_ma = max(x1,x2+1)
    if xa_ma>ma or xa_mi>mi: return "RICHARD"
    if xb_ma>ma or xb_mi>mi: return "RICHARD"
    #"""
    return "GABRIEL"
       
fRes = open("res.txt", "w")
case=0
for x,r,c in P:
    print(x,r,c)
    case+=1
    sol = solve(x,r,c)
    print("Case #{}: {}".format(case,sol))
    fRes.write("Case #{}: {}\n".format(case,sol))
        
fRes.close()