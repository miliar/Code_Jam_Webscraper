import itertools, math
def fnc(x):
    return x[1]

f = open('i1.txt', 'r')
g = open('o1.txt', 'w')
lines = f.readlines()
c = 1
Pi = math.pi
for t in xrange(int(lines[0].strip())):
    n, k = map(int, lines[c].split())
    c += 1
    ha = []
    mr = 0
    mh = 0
    mri = None
    for _ in range(n):
        rr, hh = map(int, lines[c].split())
        c += 1        
        ha.append((rr*hh, rr, hh, _))
        if (mr < rr):
            mr = rr
            mrh = hh
            mri = _
            
    ha.sort(reverse = True)
    #print ha, '->', 
    ha = ha[:k]
    mra = mr**2
    #print ha, 'and', mri
    flag = False
    for v, r, h, i in ha:
        if i == mri:
            flag = True
            break
    if (flag):
        ans = 0
        for v, r, h, i in ha:
            ans += v
        ans *= 2
        ans += mra
        #print ans, ans*Pi,  '<<'
    else:
        ha2 = ha[:-1]
        ha2.append((mrh*mr, mr, mrh, mri))
        ans1 = 0
        for v, r, h, i in ha2:
            ans1 += v
        ans1 *= 2
        ans1 += mra
        #print ans1, ans1*Pi,  '<<1'
        
        mr = max(ha, key = fnc)[1]
        mra = mr**2
        ans2 = 0
        for v, r, h, i in ha:
            ans2 += v
        ans2 *= 2
        ans2 += mra
        #print ans2, ans2*Pi,  '<<2'

        ans = max(ans1, ans2)
    print ans*Pi    
    g.write("Case #"+str(t+1)+": "+str(ans*Pi)+'\n')
    #print ''
f.close()
g.close()
