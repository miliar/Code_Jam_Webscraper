def solve(a1,a2):
    r = 0
    res = a1
    for i in a2:
        d = i.split('/')[1:]
        a = '/'+d[0]
        if a not in res:
            r = r + 1
            res.append(a)
        for k in d[1:]:
            a = a + '/' + k
            if a not in res:
                r = r + 1
                res.append(a)
    return r

f = open('A-large.in','r')
c = 0
n = 0
m = 0
c1 = 0
p1 = []
p2 = []
cd = 0
for r in f:
    r = r.strip('\n')
    d = r.split(' ')
    if c!=0 and len(d)==2:
        n = int(d[0])
        m = int(d[1])
        c1 = 0
        if cd!=0:
            print "Case #%d: %d" %(cd, solve(p1,p2),)
        p1 = []
        p2 = []
        cd = cd + 1
    elif c!=0:
        if c1<n:
            # This is the stuff already present
            p1.append(r) 
        else:
            # These are the ones to calculate for
            p2.append(r)
        c1 = c1 + 1 
    c = c + 1
print "Case #%d: %d" %(cd, solve(p1,p2),)
f.close()
