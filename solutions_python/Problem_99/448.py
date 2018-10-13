#!/bin/python
import sys

def readint(): return int(raw_input())

def readfloat(): return float(raw_input())

def readints(): return [ int(x) for x in raw_input().split() ]

def readfloats(): return [ float(x) for x in raw_input().split() ]


def mypos(m):
    for y,l in enumerate(m):
        for x,s in enumerate(l):
            if s == "X":
                return x,y

def inrange(d, mx,my, tx,ty):
    if 0 < (mx-tx)**2 + (my-ty)**2 <= d**2:
        return True

def subv(x1,y1, x2,y2):
    return (x1-x2,y1-y2)

def addv(x1,y1,x2,y2):
    return (x1+x2,y1+y2)

def dotproduct(x1, y1, x2, y2):
    return x1*x2+y1*y2

def dualrange(s,e):
    if s <= e:
        return range(s,e+1)
    else:
        return range(s,e-1,-1)

def middualrange(s,e):
    if s <= e:
        return [s] + [x + 0.5 for x in range(s, e, 1)] + [e]
    else:
        return [s] + [x - 0.5 for x in range(s, e, -1)] + [e]

def serange(lst):
    return zip(lst[:-1],lst[1:])

def calcy(slope, sx, sy, cx):
    return slope * (cx-sx) + sy

def center(a, b):
    avg = float(a+b)/2
    if avg < 0:
        return int(avg-0.5)
    else:
        return int(avg+0.5)

def rayPositions(mx,my,tx,ty):
    cx, cy = mx,my
    if mx == tx:
        for y in dualrange(my, ty):
            yield (mx,y)
        return
    slope = float(ty-my)/float(tx-mx)
    for sx, ex in serange(middualrange(mx, tx)):
        cx = center(sx,ex)
        sy = calcy(slope, mx, my, sx)
        ey = calcy(slope, mx, my, ex)
        print "#", sx, sy, "to", ex, ey
        rng = dualrange(int(sy), int(ey))
        if int(sy+0.5) == sy+0.5 and int(sx+0.5)==sx+0.5:
            rng = rng[1:]
        for cy in rng:
            print (cx,cy)
            yield (cx, cy)

def makevecs(mx, my, tx, ty):
    """
    >>> makevecs(0, 0, 1, 1)
    [(1, 0), (0, 1), (1, 1)]
    >>> makevecs(0, 0, 1, 0)
    [(1, 0)]
    >>> makevecs(0, 0, -20, -10)
    [(-1, 0), (0, -1), (-1, -1)]
    """
    vx = tx - mx
    vy = ty - my
    if vx != 0:
        nx = vx / abs(vx)
        if vy != 0:
            ny = vy / abs(vy)
            return [(nx, 0), (0, ny), (nx, ny)]
        else:
            return [(nx, 0)]
    else:
        if vy != 0:
            ny = vy / abs(vy)
            return [(0, ny)]
        else:
            raise Exception()

def addv(a, b):
    return (a[0]+b[0], a[1]+b[1])

def subv(a, b):
    return (a[0]-b[0], a[1]-b[1])

def mulv(a, x):
    return (a[0]*x, a[1]*x)

def dotv(a, b):
    return a[0]*b[0]+a[1]*b[1]

def crossv(a, b):
    return a[0]*b[1]-a[1]*b[0]

def makecorner(a):
    return [addv(a, mulv(v, 0.5)) for v in  [(1, 1), (-1, 1), (1, -1), (-1, -1)]]

def onRay(n, s, e):
    """
    >>> onRay((1,1), (0,0), (2,2))
    True
    """
    rv = subv(e,s)
    ret = []
    cn = 0
    cp = 0
    for v in makecorner(subv(n,s)):
        s = crossv(v, rv)
        if s < 0:
            cn += 1
        if 0 < s:
            cp += 1
    return 0 < cn and 0 < cp

def rayPositions(mx,my,tx,ty):
    """
    >>> [_ for _ in rayPositions(-1,-1, 2,2)]
    [(-1, -1), (0, 0), (1, 1), (2, 2)]
    >>> [_ for _ in rayPositions(0,0, -2,-2)]
    [(0, 0), (-1, -1), (-2, -2)]
    >>> [_ for _ in rayPositions(0,0, 2,-2)]
    [(0, 0), (1, -1), (2, -2)]
    >>> [_ for _ in rayPositions(0,0,1,2)]
    [(0, 0), (0, 1), (1, 1), (1, 2)]
    >>> [_ for _ in rayPositions(0,0,-1,-2)]
    [(0, 0), (0, -1), (-1, -1), (-1, -2)]
    >>> [_ for _ in rayPositions(0,0,-1,2)]
    [(0, 0), (0, 1), (-1, 1), (-1, 2)]
    """
    vecs = makevecs(mx,my,tx,ty)
    m = (mx, my)
    c = m
    t = (tx, ty)
    yield m
    while c != t:
        for v in vecs:
            n = addv(c,v)
            if onRay(n, m, t):
                c = n
                yield n
                break
        else:
            raise Exception()

def ismirror(pos, m):
    return m[pos[1]][pos[0]] == "#"

def makeMap(m):
    def test(p):
        return m[p[1]][p[0]]
    return test

def revx(v):
    return (-v[0],v[1])
def revy(v):
    return (v[0],-v[1])

def makeMirrorWorld(s, e, m):
    v = subv(e,s)
    if v[1] == 0:
        def newWorld(p):
            return m(addv(revx(subv(p,e)),s))
        return newWorld
    elif v[0] == 0:
        def newWorld(p):
            return m(addv(revy(subv(p,e)),s))
        return newWorld
    else:
        jx = m(addv(s,(v[0], 0)))=="#"
        jy = m(addv(s,(0,v[1])))=="#"
        jxy = m(addv(s,v))=="#"
        if jx and jy and jxy:
            def newWorld(p):
                return m(addv(revx(revy(subv(p,e))),s))
            return newWorld
        elif jx and jxy:
            return lambda p: m(addv(revx(subv(p,e)),addv(s,(0,v[1]))))
        elif jy and jxy:
            return lambda p: m(addv(revy(subv(p,e)),addv(s,(v[0],0))))
        elif jxy:
            return lambda p: "."
        else:
            raise Exception()

def isSelfPos(mx,my,tx,ty,m):
    """
    >>> isSelfPos(1, 1, -1, 3, ['###', '#X#', '#.#', '###'])
    False

    >>> isSelfPos(1, 1, 5, 1, ['####', '#X.#', '####'])
    False
    >>> isSelfPos(1, 1, 2, 1, ['###', '#X#', '###'])
    True
    >>> isSelfPos(1, 1, 2, 1, ['####', '#X.#', '####'])
    False
    >>> isSelfPos(1, 1, 3, 1, ['####', '#X.#', '####'])
    False

    >>> isSelfPos(1, 1, 1, -2, ['###', '#X#', '#.#','###'])
    False
    >>> isSelfPos(1, 1, 1, -3, ['###', '#X#', '#.#','###'])
    False
    >>> isSelfPos(1, 1, 1, -4, ['###', '#X#', '#.#','###'])
    False

    """
    m = makeMap(m)
    for s, e in serange([_ for _ in rayPositions(mx,my,tx,ty)]):
        if m(e) == "#":
            m = makeMirrorWorld(s, e, m)
        if e != (tx, ty) and m(e) == "X" and crossv(subv(e, (mx,my)),subv((tx,ty),(mx,my))) == 0:
            return False
    return m((tx,ty)) == "X"

def iteratePatterns(a,ps):
    import itertools
    for ptn in itertools.product( *[[True,False]]*a):
        ret = 1.0
        for f, p in zip(ptn, ps):
            if f:
                ret *= p
            else:
                ret *= 1.0-p
        yield ret, ptn

def solve(a,b,ps):
    import itertools
    rets = []
    
    # n back
    for back in range(a):
        ret = []
        ps2 = ps
        if back != 0:
            ps2 = ps[:-back]
        for p, ptn in iteratePatterns(int(a-back),ps2):
            if len([ _ for _ in ptn if not _ ]) == 0:
                ret.append( ((back+(b-(a-back))+1), p))
            else:
                ret.append( ((back+(b-(a-back))+1+b+1), p))
        ret = [ i*j for i,j in ret ]
        rets.append(sum(ret))
    # enter
    rets.append(1+b+1)
    return min(rets)

if __name__ == "__main__":
    inputname = "A-small-attempt0.in"
    sys.stdin = file(inputname)
    f = file(inputname + ".out.txt","w")

    if False:
        import doctest
        doctest.testmod()
        import sys
        sys.exit(0)
    
    nt = readint()
    for i in range(nt):
        a, b = tuple(readints())
        ps = tuple(readfloats())
        result = "Case #%d: %.6f" % ( i+1, solve(a,b,ps))
        print result
        print >>f,result
    f.close()
