# -*- coding: utf-8 -*-

fname1 = 'C-small-attempt0'
f1 = open(fname1 + '.in','r')
cases = int(f1.readline())
f2 = open(fname1 + '.out','w')
for case in range(cases):
    R, k, n = map(int, str(f1.readline()).split(' '))
    g = map(int,str(f1.readline()).split(' '))
    M = 0
    while (R >= 1):
        j = k
        i = 0
        while (j >= g[i]):
            M += g[i]
            j -= g[i]
            if (i < (n - 1)):
                i += 1
            else: 
                break
        g = g[i:] + g[:i]
        R -= 1
    #print 'Case #%s: %s\n' % (case + 1, M)
    f2.write('Case #%s: %s\n' % (case + 1, M))
f1.close()
f2.close()