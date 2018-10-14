from fractions import gcd

def getint(): return int(input())
def getlist(what): return list(map(what, input().split()))

T = getint()
for test in range(1, T+1):
    l = getlist(int)
    l.pop(0)
    g = -1
    for i in l:
        if l[0] != i:
            if g == -1:
                g = abs(l[0]-i)
            else:
                g = gcd(g, abs(l[0]-i))
    if g == -1:
        g = 0            
    print("Case #%d: " % test, end='')
    if g > 1: print((g-(l[0]%g))%g)
    else: print(0)
    
