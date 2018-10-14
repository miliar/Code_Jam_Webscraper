def path(start,stop,a,b):
    if b > 1:
        return b
    if start == stop:
        return b + 1
    i = 0
    k = 0
    while True:
        if start == k:
            break
        k += 1
        i += a[i]+1
    if a[i] == 0:
        return b
    for x in xrange(i+1,i+1+a[i]):
        b = path(a[x]-1,stop,a,b)
    return b    

t = int(raw_input())
for x in xrange(t):
    n = int(raw_input())
    m = []
    for i in xrange(n):
        a = raw_input()
        a = a.split()
        a = map(int,a)
        m = m + a
    for start in xrange(n):
        flag = 0
        for end in xrange(n):
            k = start
            flag = path(k,end,m,0)
            if flag > 1 :
                break
        if flag > 1:
            break
    if flag > 1:
        print "Case #%d: Yes"%(x+1)
    else:
        print "Case #%d: No"%(x+1)
            
            
        
