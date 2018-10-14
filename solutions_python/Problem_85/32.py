def solve(): 
    ax = map(int,raw_input().split())
    l,t,n,c = ax[:4]
    a = ax[4:]
    a = [x*2 for x in a]
    a = (a * (n/c+1))[:n]
    ss = sum(a)
    s = 0
    for i in xrange(n):
        if s+a[i]>t: break
        s+=a[i]
    else:
        if t>=s: return s
    a[i]-=t-s
    a=a[i:]
    a.sort(reverse=True)
    return ss-sum(a[:l])/2

t = input()
for tn in xrange(t):
    r = solve()
    print "Case #%d:"%(tn+1),r

