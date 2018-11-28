'''
Created on 12/04/2014

@author: david
'''

#f=open("exampleA.txt")
#f=open("A-small-attempt0.in")
f=open("A-large.in")

T=int(f.readline())
P=[]
for i in range(T):
    p = [int(n) for n in f.readline().split()[1]]
    P.append(p)

def solve(p):
    f = 0
    a = 0
    for sl,np in enumerate(p):
        if sl>a:
            f += (sl-a)
            a += (sl-a)
        a += np
    
    return f
       
fRes = open("res.txt", "w")
case=0
for p in P:
    print(p)
    case+=1
    sol = solve(p)
    print("Case #{}: {}".format(case,sol))
    fRes.write("Case #{}: {}\n".format(case,sol))
        
fRes.close()