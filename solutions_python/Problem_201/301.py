from __future__ import print_function
s = """5
267 256
267 1
267 2
267 11
267 12
1000 2"""

s = open('C-large.in').read()
import sys
import math
ss = s.split('\n')
T = int(ss[0])
f = open('C.out', 'w')
# f = sys.stdout

def calc(x):
    if x == 1:
        return 0, 0
    if x % 2 == 0:
        return x/2, (x-1)/2
    else:
        return (x-1)/2, (x-1)/2

for i in range(0, T):
    # print('-----')
    cs = ss[i+1].split(' ')
    N = int(cs[0])
    K = int(cs[1])
    # print('N=%d'%(N))
    if K == 1:
        m, n = calc(N)
        print('Case #%d: %d %d' % (i+1, m, n), file=f)
    else:
        T = N
        m, n = calc(T)
        if m == n:
            cM, cN = 2, 0
        else:
            cM, cN = 1, 1
        LevelI = 1
        while(T > 0):
            K -= LevelI
            LevelI *= 2
            if K <= LevelI:
                if K <= cM:
                    a, b = calc(m)
                    print('Case #%d: %d %d' % (i + 1, a, b), file=f)
                else:
                    a, b = calc(n)
                    print('Case #%d: %d %d' % (i + 1, a, b), file=f)
                break
            last_m, last_n = m, n
            last_cM, last_cN = cM, cN
            cM, cN = 0, 0
            if m == n:
                m, n = calc(m)
                if m == n:
                    cM += last_cM * 2
                else:
                    cM += last_cM
                    cN += last_cM
            else:
                if last_m % 2 == 0:
                    m, n = calc(last_m)
                    tm, tn = calc(last_n)
                    cM += last_cM
                    cN += last_cM
                    if tm == m:
                        cM += 2*last_cN
                    else:
                        cN += 2*last_cN
                else:
                    m, n = calc(last_n)
                    tm, tn = calc(last_m)
                    cM += last_cN
                    cN += last_cN
                    if tm == m:
                        cM += 2 * last_cM
                    else:
                        cN += 2 * last_cM
            T = m

            # print('m=%d,n=%d,cM=%d,cN=%d, K=%d' % (m, n, cM, cN, K))