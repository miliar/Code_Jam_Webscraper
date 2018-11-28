#!/usr/bin/env python
#coding=utf-8
#!/usr/bin/env python
#coding=utf-8

import math


def seive(n):
    assert n > 1
    pl = [2]
    ln = (n-1)/2
    cad = [1]*ln
    for i in xrange(ln):
        if cad[i] == 1:
            p = 2*i+3
            pl.append(p)
            for j in xrange(i+p,ln, p):
                cad[j] = 0
    return pl


def is_prime(n, pl=[], ext=False):
    assert n > 0
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    if n in pl:
        return True
    if len(pl)>0 and n < pl[-1]:
        return False
    r = math.floor(n**0.5)
    for p in pl:
        if p > r:
            return True
        if n%p == 0:
            return False
    cad = len(pl) and (pl[-1]+2) or 3
    if ext and len(pl) == 0:
        pl.append(2)
    while cad <= r:
        if ext and is_prime(cad, pl, ext):
            pl.append(cad)
        if n%cad == 0:
            return False
        cad += 2
    return True


def iter_factorial(n):
    assert n >= 0
    if n == 0:
        yield 1
        raise StopIteration
    i = 1
    m = 1
    while i < n:
        yield m
        i += 1
        m *= i
    raise StopIteration


def iter_permutation(n, m):
    assert n >= 0
    assert m >= 0
    assert n >= m
    shadow = [1]*n
    nexti = 0
    cad = []
    while True:
        if nexti < n:
            if shadow[nexti] == 1:
                shadow[nexti] = 0
                cad.append(nexti)
                if len(cad) == m:
                    yield cad
                    nexti = cad.pop()
                    shadow[nexti] = 1
                else:
                    nexti = -1
            nexti += 1
        elif len(cad) == 0:
            break
        else:
            nexti = cad.pop()
            shadow[nexti] = 1
            nexti += 1
    raise StopIteration


def iter_combination(n, m):
    assert n >= 0
    assert m >= 0
    assert n >= m
    if m == n:
        yield range(n)
        raise StopIteration
    shadow = [1]*n
    static = range(n)
    nexti = 0
    cad = []
    ln = 0
    while True:
        if nexti < n:
            if shadow[nexti] == 1:
                shadow[nexti] = 0
                cad.append(nexti)
                ln += 1
                if ln == m:
                    yield cad
                    nexti = cad.pop()
                    ln -= 1
                    shadow[nexti] = 1
            nexti += 1
        elif ln == 0:
            break
        else:
            nexti = cad.pop()
            ln -= 1
            shadow[nexti] = 1
            if m-ln > n-nexti-1:
                nexti = n
            else:
                nexti += 1
    raise StopIteration


def iter_BFS(matrix, root=0):
    n = len(matrix)
    assert n > 0
    for i in xrange(n):
        assert len(matrix[i]) == n
    visit = [False]*n
    queue = []
    qlen = 0
    visit[root] = True
    queue.append(root)
    qlen += 1
    yield root
    while qlen != 0:
        current = queue.pop(0)
        qlen -= 1
        for i in xrange(n):
            if matrix[current][i] != 0:
                if not visit[i]:
                    visit[i] = True
                    queue.append(i)
                    qlen += 1
                    yield i
    raise StopIteration


def iter_DFS(matrix, root=0):
    n = len(matrix)
    assert n > 0
    for i in xrange(n):
        assert len(matrix[i]) == n
    visit = [False]*n
    queue = []
    qlen = 0
    visit[root] = True
    queue.append(root)
    qlen += 1
    yield root
    current = root
    nexti = 0
    while True:
        nonext = True
        for i in xrange(nexti, n):
            if matrix[current][i] != 0 and not visit[i]:
                visit[i] = True
                queue.append(i)
                qlen += 1
                current = i
                yield current
                nonext = False
                nexti = 0
                break
        if nonext:
            nexti = queue.pop()
            qlen -= 1
            if qlen == 0:
                raise StopIteration
            else:
                current = queue[-1]


def B():
    test = False
    sample = """3
2
2
1 2 1
2 1 1 2 0
5
3
1 1 1
2 1 0 2 0
1 5 0
1
2
1 1 0
1 1 1"""
    infile = iter(sample.split('\n'))
    if not test:
        infile = open("B-small-attempt1.in",'r')
    outfile = open("B-small-attempt1.out",'w')
    N = int(infile.next())
    for n in xrange(N):
        fn = int(infile.next())
        cn = int(infile.next())
        cf = []
        for i in xrange(cn):
            cf.append([int(x) for x in infile.next().split()])
        best = 2**fn-1
        bc = fn
        impossible = True
        for mask in xrange(2**fn):
            mimp = False
            for c in cf:
                cimp = True
                for i in xrange(c[0]):
                    if 0 == (((mask >> (c[2*i+1]-1)) & 1) ^ c[2*i+2]):
                        cimp = False
                        break
                if cimp:
                    mimp = True
                    break
            if not mimp:
                impossible = False
                i = 1
                tc = 0
                while i < 2**fn:
                    if (i & mask) != 0:
                        tc += 1
                    i = i << 1
                if tc < bc:
                    best = mask
                    bc = tc
        case_out = "Case #%d: "%(n+1)
        if impossible:
            case_out += "IMPOSSIBLE"
        else:
            for i in xrange(fn):
                best, r = divmod(best,2)
                case_out += str(r)+' '
        print case_out
        outfile.write(case_out+'\n')
    if not test:
        infile.close()
    outfile.close()

if __name__ == '__main__':
    import time
    start = time.clock()
    B()
    print "done in %f"%(time.clock()-start)
