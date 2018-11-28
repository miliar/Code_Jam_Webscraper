
def mul((sa, a), (sb, b)):
    s = sa * sb
    if a == '1':
        return s, b
    if b == '1':
        return s, a
    if a == b:
        return -s, '1'
    if a == 'i':
        if b == 'j':
            return s, 'k'
        if b == 'k':
            return -s, 'j'
        error
    if a == 'j':
        if b == 'i':
            return -s, 'k'
        if b == 'k':
            return s, 'i'
        error
    if a == 'k':
        if b == 'i':
            return s, 'j'
        if b == 'j':
            return -s, 'i'
        error
    error

def makeit(ss):
    # print ss
    if len(ss) < 3:
        return False
    tab = [ (1, '1') ]
    for i in xrange(len(ss)):
        c = ss[i]
        tab.append(mul(tab[-1], (1, c)))
    n = len(tab)
    if tab[-1] != (-1, '1'):
        return False
    # print tab
    for i in xrange(n):
        if tab[i] == (1, 'i'):
            for j in xrange(i + 1, n):
                if tab[j] == (1, 'k'):
                    # print ss[:i], ss[i:j], s[j:]
                    return True
    return False

import sys
readline = sys.stdin.readline

T = int(readline().strip())

for t in xrange(1, T + 1):
    L, X = readline().split()
    L, X = int(L), int(X)
    seq = readline().strip()
    assert len(seq) == L
    s = seq * X
    res = makeit(s)
    if res:
        print "Case #%d: YES" % t
    else:
        print "Case #%d: NO" % t
