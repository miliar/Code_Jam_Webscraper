'''
Created on Apr 9, 2016

@author: david
'''
#f=open("exampleB.txt")
#f=open("B-small-attempt0.in")
f=open("B-large.in")

T=int(f.readline())
P=[]
for i in range(T):
    s = f.readline().strip()
    P.append(s)

def rev(o):
    if o=='+': return '-'
    return '+'

def is_ok(s):
    p='0'
    nt = []
    for i,c in enumerate(s):
        if c>=p:
            p=c
            continue
        return False
    return True

def repair(n):
    n -= 1
    r = ''
    while n>0 and not is_ok(str(n)):
        r += '9'
        n //= 10
        n -= 1
    if n == 0: return r
    return str(n)+r 
        
def solve(ss):
    p='0'
    nt = []
    for i,c in enumerate(ss):
        if c>=p:
            p=c
            nt.append(c)
            continue
        return repair(int(''.join(nt)))+'9'*len(ss[i:])
    else:
        return ss
        
fRes = open("res.txt", "w")
case=0
for s in P:
    print(s)
    case+=1
    sol = solve(s)
    print("Case #{}: {}".format(case,sol))
    fRes.write("Case #{}: {}\n".format(case,sol))
        
fRes.close()