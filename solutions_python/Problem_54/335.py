from fractions import gcd

def readint(): return int(raw_input())
def readarray(f): return map(f,raw_input().split())

def solve(N,tlist):
    tlist.sort()
    mini=0
    l=len(tlist)
    mindiff=None
    for i in xrange(0,l-1):
        if mindiff == None or mindiff > (abs(tlist[i+1] - tlist[i])):
            mindiff = abs(tlist[i+1] - tlist[i])
            mini = i
    difflist=[]
    for i,t in enumerate(tlist):
        if i == mini: continue
        difflist.append(abs(t-tlist[mini]))
    mingcd=mindiff
    for d in difflist:
        g = gcd(d,mingcd)
        if g < mingcd:
            mingcd = g
    res = tlist[mini] % mingcd
    if res == 0:
        return 0
    else:
        return mingcd - res
    
        

C = readint()
for c in xrange(C):
    tlist = readarray(int)
    N = tlist.pop(0)
    tlist2 = list(set(tlist))
    ans = solve(N,tlist2)
    print "Case #%d: %d" % (c+1,ans)
                
