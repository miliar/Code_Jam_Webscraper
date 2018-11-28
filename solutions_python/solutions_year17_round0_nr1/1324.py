def inv(st,k_val):
    if k_val>len(st):
        return st
    tans = st[k_val:]
    d = {'+':'-','-':'+'}
    for i in xrange(k_val-1,-1,-1):
        tans = d[st[i]]+tans
    return tans
for i in range(input()):
    ans = None
    s,k = raw_input().strip().split()
    k = int(k)
    if s.count('-')==0:
        ans = 0
    elif k==1:
        ans = s.count('-')
    else:
        l = len(s)
        s = s.lstrip('+')
        s = inv(s,k)
        #print s
        ans = 1
        s = s.lstrip('+')
        #print s
        while len(s)>0:
            if len(s)==l:
                ans = "IMPOSSIBLE"
                break
            l = len(s)
            s = inv(s,k)
            #print s
            s = s.lstrip('+')
            ans += 1   
            #print s
    print "Case #{}: {}".format(i+1,ans)