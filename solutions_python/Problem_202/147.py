# -*- coding: utf-8 -*-
"""
@author: jmzhao
GCJ 2017 Qualification Round
"""

from itertools import chain, product
import sys

class IO :
    def get(reader=str) :
        return reader(input().strip())
    def gets(reader=str, delim=None) :
        return [reader(x) for x in input().strip().split(delim)]
    def tostr(raw, writer=str, delim=' ') :
        return delim.join(writer(x) for x in raw)

def prework(argv):
    '''do something according to argv,
    return a message describing what have been done.'''
    pass


def once():
    '''to cope once
    return the answer to be printed'''
    n, m = IO.gets(int)
    a = [['.'] * n for _ in range(n)]
    for _ in range(m) :
        char, r, c = IO.gets()
        r, c = int(r) - 1, int(c) - 1
        a[r][c] = char

    x_r, x_c = set(), set()
    p_m, p_p = set(), set()
    for i in range(n) :
        for j in range(n) :
            if a[i][j] in 'xo' :
                x_r.add(i)
                x_c.add(j)
            if a[i][j] in '+o' :
                p_m.add(i - j)
                p_p.add(i + j)
    
    b = [[a[i][j] for j in range(n)] for i in range(n)]
    unused_c = [c for c in range(n) if c not in x_c]
    for r in range(n) :
        if r not in x_r :
            c = unused_c.pop()
            assert b[r][c] in '.+'
            b[r][c] = 'x' if b[r][c] in '.' else 'o'
    for m in chain(range(- (n - 1), 0), reversed(range(n))) :
        if m not in p_m :
            for p in range(max(m, -m), 2 * (n - 1) + min(m, -m) + 1) :
                if (p + m) % 2 == 0 and p not in p_p :
                    p_p.add(p)
                    r = (p + m) // 2
                    c = (p - m) // 2
                    assert b[r][c] in '.x'
                    b[r][c] = '+' if b[r][c] in '.' else 'o'
                    break
                
    res = [(b[i][j], i+1, j+1) for i, j in product(range(n), range(n)) if b[i][j] != a[i][j]]
    
    score_chart = {'.' : 0, '+' : 1, 'x' : 1, 'o' : 2}
    score = sum(score_chart[b[i][j]] for i, j in product(range(n), range(n)))
    
    return score, res

def show(ans) :
    score, res = ans
    return ("%d %d"%(score, len(res))
    + ('\n' if len(res) > 0 else '')
    + '\n'.join("%s %d %d"%t for t in res))
    
def printerr(*v):
    print(*v, file=sys.stderr)

def main():
    TT = IO.get(int)
    for tt in range(1,TT+1):
        printerr("coping Case %d.."%(tt))
        ans = once()
        print("Case #%d: %s"%(tt, show(ans)))

if __name__ == '__main__' :
    msg = prework(sys.argv)
    print("prework done with", msg, file=sys.stderr)
    main()
