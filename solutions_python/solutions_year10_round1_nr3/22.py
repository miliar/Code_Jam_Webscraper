import sys

getline = sys.stdin.readline

cache = {}
def dfs(a, b):
    if a<=0 or b<=0:
        return True
    if a > b:
        a, b = b, a
    
    # cache
    if (a,b) in cache:
        return cache[(a,b)]
    
    d = b/a
    if d > 1:
        res = not dfs(a, b-a*d) or not dfs(a, b-a*(d-1))
    else:
        res = not dfs(a, b-a*d)
    cache[(a,b)] = res
    return res

def tc(I):
    res = 0
    a1, a2, b1, b2 = [int(x.strip()) for x in getline().split()]
    for a in range(a1, a2+1):
        #print "%d" % a
        for b in range(b1, b2+1):
            if dfs(a,b):
                res += 1
                #print "%d ok: (%d, %d)" % (I, a,b)
    print "Case #%d: %d" % (I, res)

T = int(getline()) 
for i in range(T):
    tc(i+1)
