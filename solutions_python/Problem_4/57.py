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


def A():
    test = False
    sample = """2
3
1 3 -5
-2 4 1
5
1 2 3 4 5
1 0 1 0 1"""
    infile = iter(sample.split('\n'))
    if not test:
        infile = open("A-large.in",'r')
    outfile = open("A-large.out",'w')
    N = int(infile.next())
    for n in xrange(N):
        case_out = "Case #%d: "%(n)
        ln = int(infile.next())
        v1 = [int(x) for x in infile.next().split()]
        v2 = [int(x) for x in infile.next().split()]
        v1.sort()
        v2.sort(reverse=True)
        #print v1
        #print v2
        rslt = sum([v1[i]*v2[i] for i in xrange(ln)])
        case_out = "Case #%d: %d"%(n+1, rslt)
        print case_out
        outfile.write(case_out+'\n')
    if not test:
        infile.close()
    outfile.close()

if __name__ == '__main__':
    import time
    start = time.clock()
    A()
    print "done in %f"%(time.clock()-start)
