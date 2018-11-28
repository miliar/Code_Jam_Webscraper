#!/usr/bin/env python2

f = open('i', 'r')

n = int(f.readline()[:-1])

for i in range(n):
    s = f.readline()[:-1]
    ary = s.split(' ')
    a = int(ary[0])
    b = int(ary[1])
    cnt = 0
    for j in range(a,b+1):
        n = str(j)
        l = len(n)
        s = {}
        for k in range(1, l):
            if n[k] < n[0]:
                continue
            m = n[k:] + n[0:k]
            M = int(m)
            if M >= a and M <= b:
                if M > j and not s.has_key(m):
                    cnt += 1
                    s[m] = True
                    
    print 'Case #%d: %d' % (i+1, cnt)
