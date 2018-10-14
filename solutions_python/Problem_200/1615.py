t = int(raw_input())
for case in xrange(1, t+1):
    n = map(int, list(raw_input()))
    start_9 = -1
    last_c = 10
    for i in xrange(len(n)):
        idx = len(n) - i - 1
        c = n[idx]
        if c > last_c:
            start_9 = idx+1
            last_c = c-1
            n[idx] = c-1
        else:
            last_c = c
    print "Case #"+str(case)+":",
    if start_9 == -1:
        print ''.join(map(str, n))
    else:
        for i in xrange(start_9, len(n)):
            n[i] = 9
        print ''.join(map(str, n)).lstrip("0")

            
