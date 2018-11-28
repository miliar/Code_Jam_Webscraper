'''
Created on Apr 9, 2016

@author: david
'''
#f=open("exampleA.txt")
#f=open("A-small-attempt1.in")
f=open("A-large.in")

T=int(f.readline())
P=[]
for i in range(T):
    s, n = f.readline().split()
    k = int(n)
    P.append((list(s),k))

def rev(o):
    if o=='+': return '-'
    return '+'

def solve(s, k):
    n=0
    for i,c in enumerate(s):
        if i>=len(s)-k+1:
            for j in range(i, len(s)):
                if s[j] != '+':
                    return "IMPOSSIBLE"
            return n
        if c == '+': continue
        for jj in range(i, i+k):
            s[jj]=rev(s[jj])
        n+=1
    return n
        
fRes = open("res.txt", "w")
case=0
for s,k in P:
    print(len(s),k)
    case+=1
    sol = solve(s,k)
    print("Case #{}: {}".format(case,sol))
    fRes.write("Case #{}: {}\n".format(case,sol))
        
fRes.close()