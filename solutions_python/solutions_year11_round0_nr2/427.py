from collections import defaultdict

t = input()

def solve():
    d = defaultdict(int)
    o = defaultdict(list)
    cb = {}
    s = raw_input().split()
    c = int(s[0])
    for a in s[1:1+c]:
        cb[a[:2]]=a[2]
        cb[a[1::-1]]=a[2]    
    s = s[1+c:]
    dd = int(s[0])
    for a in s[1:1+dd]:
        o[a[0]].append(a[1])
        o[a[1]].append(a[0])
    s = s[-1]
    l = []
    for c in s:
        while l and (l[-1]+c) in cb:
            d[l[-1]]-=1
            c = cb[(l[-1]+c)]
            l.pop()
        for h in o[c]:
            if d[h]:
                d = defaultdict(int)
                l = []
                break
        else:
            l.append(c)
            d[c]+=1        
    return ', '.join(l)

for i in xrange(t):
    print "Case #%d: [%s]"%(i+1,solve())
        