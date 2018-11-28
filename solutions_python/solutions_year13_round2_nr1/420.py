t = int(raw_input())
for ab in xrange(t):
    x = map(int,raw_input().split())
    a = x[0]
    n = x[1]
    size = map(int,raw_input().split())
    size.sort()
    s = a
    for i in xrange(n):
        if size[i] < s :
            s += size[i]
        else :
            break
    temp = s
    best = n-i
    if s-1 == 0:
        count = n-i
    else :
        for k in xrange(0,n-i+1):
            s = temp
            count = k
            m = i
            while m < n-k:
                while s <= size[m]:
                    s = s + (s-1)
                    count += 1
                while s > size[m] :
                    s += size[m]
                    m += 1
                    if m == n-k:
                        break
            if count < best :
                best = count
                kik = k
    print "Case #%d: %d" %(ab+1,best)

