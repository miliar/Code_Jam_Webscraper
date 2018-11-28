def rotate(s,l,u):
    res = []
    for i in range(1,len(s)):
        r = s[-i:] + s[:-i]
        if r.startswith('0'):
            continue
        if (r >= l) and ( r <= u):
            if s < r:
                res.append((s,r))
            elif s > r: # NO equal sign
                res.append((r,s))
    return res
    
T = int(raw_input())

for n in range(T):
    res = []
    A,B = [int(i) for i in raw_input().split()]
    sA, sB = str(A), str(B)
    for t in range(A,B+1):
        res.extend(rotate(str(t),sA,sB))
    
    print 'Case #%d: %d' % (n+1, len(set(res)))