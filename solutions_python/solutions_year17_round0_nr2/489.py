t = int(raw_input())
for a in xrange(t):
    n = raw_input().replace('\r', '')
    n = [int(i) for i in n]
    for i in xrange(len(n)-1):
        if n[i] <= n[i+1]: continue
        break
    else:
        print 'Case #%d: %s' % (a+1, ''.join([str(i) for i in n]))
        continue
    for j in xrange(i+1, len(n)):
        n[j] = 9
    while True:
        n[i] -= 1
        if i == 0:
            if n[i] == 0: n = n[1:]
            break
        else:
            if n[i-1] <= n[i]: break
            n[i] = 9
            i -= 1
    print 'Case #%d: %s' % (a+1, ''.join([str(i) for i in n]))
    