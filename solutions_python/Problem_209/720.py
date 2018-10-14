import math
import operator

def area(r) :
    return math.pi * math.pow(r,2)

def perim(r) :
    return 2 * math.pi * r

def f(p):
    return math.pow(p[0],2)+2*p[1]
def f2(p):
    return math.pow(p[0],2)

def solve(n,k,pl) :

    base = max(pl, key=f)
    spl = sorted(pl,key=operator.itemgetter(1),reverse=True)

    s=[]
    for i in range(0,k):
        s += [spl[i]]

    if base not in s :
        s= s[0:-1] + [base]

    #print(s,"!",base)

    base = max(s, key=f2)
    
    surface = area(base[0])
    for e in s :
        surface += perim(e[1])
    
    return surface

in_t = int(input())
for i in range(0, in_t) :
    n, k = input().split()
    n = int(n)
    k = int(k)
    pl = []
    for j in range(0, n):
        r, h = input().split()
        r = int(r)
        h = int(h)
        pl += [[r,r*h]]
    #print(n,"!",k,"!",pl)
    
    result = solve(n,k,pl)

    print("Case #", i+1, ": ", "%.7f" % result, sep='')
