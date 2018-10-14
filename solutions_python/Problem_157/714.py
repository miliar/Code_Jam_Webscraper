import sys
import itertools
import math
D = False
def rl():
    return map(int,raw_input().strip().split())

def solve(L, X, s):
    if D: print '====== ' + str(locals())
    q = {'11':('1',1),  'ii':('1',-1), 'jj':('1',-1), 'kk':('1',-1),
                        '1i':('i', 1), '1j':('j', 1), '1k':('k', 1),
                        'i1':('i', 1), 'ij':('k', 1), 'ik':('j',-1),
                        'j1':('j', 1), 'ji':('k',-1), 'jk':('i', 1),
                        'k1':('k', 1), 'ki':('j', 1), 'kj':('i',-1),}
    length = L*X
    if length < 3:
        return 'NO'
    if len(set(list(s))) == 1:
        return 'NO'
    if len(set(list(s))) == 2 and '1' in set(list(s)):
        return 'NO'
    ss = list(s) * X
    tmp = ss[0]
    sign = 1
    for i in xrange(1, len(ss)):
        d = q[tmp+ss[i]]
        sign *= d[1]
        tmp = d[0]
    if tmp != '1' or sign != -1:
        return 'NO'
    for i in xrange(1,length):
        tmp = ss[0]
        sss = ss[0:i]
        sign = 1
        if D: print 'i=%d' % i
        for j in xrange(1, len(sss)):
            d = q[tmp+sss[j]]
            sign *= d[1]
            tmp = d[0]
        if sign > 0 and tmp == 'i':
            p = set(list(ss[i:]))
            if len(p) == 1:
                return 'NO'
            if len(p) == 2 and '1' in p:
                return 'NO'
            for k in xrange(i,length):
                tmp = ss[i]
                sss = ss[i:k]
                sign = 1
                if D: print 'k=%d %s' % (k, sss)
                for l in xrange(1, len(sss)):
                    d = q[tmp+sss[l]]
                    sign *= d[1]
                    tmp = d[0]
                if sign > 0 and tmp == 'j':
                    tmp = ss[k]
                    sss = ss[k:]
                    sign = 1
                    if D: print 'last= %s' % sss
                    for m in xrange(1, len(sss)):
                        d = q[tmp+sss[m]]
                        sign *= d[1]
                        tmp = d[0]
                        if D: print tmp
                    if D: print 'sign=%d %s' % (sign, tmp)
                    if sign > 0 and tmp == 'k':
                        return 'YES'
    return 'NO'

if __name__ == '__main__':
    for case in range(int(raw_input())):
        l = rl()
        print 'Case #%d: %s' % (case+1, solve(l[0], l[1], raw_input().strip()))