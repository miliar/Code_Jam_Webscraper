cache = {}

def cached(f):
    def cf(*args):
        assert isinstance(args, tuple)
        c = (f, args)
        if c in cache:
            return cache[c]
        cache[c] = f(*args)
        return cache[c]
    return cf

def clearCache():
    global cache
    cache = {}


class Quad(object):
    def __init__(self, level):
        self.level = level
    def getElem(self, level, x, y):
        assert 0 <= x <= 1<<level
        assert 0 <= y <= 1<<level
        if level == 0:
            return self
        s = 1<<(level-1)
        if x < s:
            if y < s:
                return self.nw.getElem(level-1, x, y)
            else:
                return self.sw.getElem(level-1, x, y-s)
        else:
            if y < s:
                return self.ne.getElem(level-1, x-s, y)
            else:
                return self.se.getElem(level-1, x-s, y-s)

    def aliveCells(self):
        for x in range(1<<self.level):
            for y in range(1<<self.level):
                if self.getElem(self.level, x, y) == one:
                    yield x,y

one = Quad(0)
zero = Quad(0)

@cached
def getQuad(*args):
    assert args[0].level == args[1].level == args[2].level == args[3].level
    q = Quad(args[0].level+1)
    q.nw, q.ne, q.sw, q.se = args
    return q

@cached
def empty(level):
    q = zero
    for i in range(level):
        q = getQuad(q, q, q, q)
    assert q.level == level
    return q

@cached
def full(level):
    q = one
    for i in range(level):
        q = getQuad(q, q, q, q)
    assert q.level == level
    return q
    
@cached
def evolve(q, steps):
    assert q.level > 0
    assert steps <= 1<<(q.level-1)
    if steps == 0:
        return q.se
    if q.level == 1:
        assert steps == 1
        if q.ne == q.sw == zero:
            return zero
        if q.ne == q.sw == one:
            return one
        return q.se

    d = {}
    for i in range(4):
        for j in range(4):
            #if i+j <= 1:
            #    d[i, j] = empty(q.level-2)
            #    continue
            d[i, j] = q.getElem(2, i, j)

    steps1 = min(steps, 1<<(q.level-2)) 
    steps2 = max(steps-(1<<(q.level-2)), 0)
    assert steps == steps1+steps2
    d1 = {}
    for i in range(1,4):
        for j in range(1,4):
            #if i == j == 1:
            #    d1[i, j] = empty(q.level-2)
            #    continue
            d1[i, j] = evolve(getQuad(d[i-1, j-1], d[i, j-1], d[i-1, j], d[i, j]), 
                steps1)

    # print 'after steps1',steps1
    # for i in range(1,4):
        # for j in range(1,4):
            # print 'at',j,i
            # printQuad(d1[j, i])

    d2 = {}
    for i in range(2,4):
        for j in range(2,4):
            d2[i, j] = evolve(getQuad(d1[i-1, j-1], d1[i, j-1], d1[i-1, j], d1[i, j]),
                steps2)

    # print 'after steps2',steps2
    # for i in range(2,4):
        # for j in range(2,4):
            # print 'at',j,i
            # printQuad(d2[j, i])
            
            
    result = getQuad(d2[2, 2], d2[3, 2], d2[2, 3], d2[3, 3])
    
    if False:
        # slow check
        newCells = naiveEvolve(q.aliveCells(), steps)
        s = 1<<(q.level-1)
        newCells = [(x-s,y-s) for x,y in newCells if x >= s and y >= s]
        s1 = set(newCells)
        s2 = set(result.aliveCells())
        assert s1 == s2, (s1,s2)
    
    return result


def naiveEvolve(cells, steps = 1):
    cells = set(cells)
    sx = sy = 1
    for x, y in cells:
        sx = max(sx, x+1)
        sy = max(sy, y+1)
    for step in range(steps):
        newCells = set()
        for x in range(sx):
            for y in range(sy):
                b = (x,y) in cells
                b1 = (x,y-1) in cells
                b2 = (x-1,y) in cells
                if b+b1+b2 >= 2:
                    newCells.add((x,y))
        cells = newCells
    return cells
#    for step in range(steps):
    
def printCells(q):
    #sx = 1<<q.level
    #sy = 1<<q.level
    sx = sy = 1
    c = {}
    for x, y in q:
        c[x, y] = 1
        sx = max(sx, x+1)
        sy = max(sy, y+1)

    for y in range(sy):
        for x in range(sx):
            if (x,y) in c:
                print 1,
            else:
                print 0,
        print

def printQuad(q):
    printCells(q.aliveCells())
    

zeroOne = [zero, one]
    
@cached
def quadMap(f, *quads):
    q = quads[0]
    if q.level == 0:
        return zeroOne[f(*map(zeroOne.index, quads))]
        
    return getQuad(
        quadMap(f,*[q.nw for q in quads]),
        quadMap(f,*[q.ne for q in quads]),
        quadMap(f,*[q.sw for q in quads]),
        quadMap(f,*[q.se for q in quads]),
        )

@cached
def leftPart(level,w):
    if level == 0:
        if w <= 0:
            return zero
        return one
    return getQuad(
        leftPart(level-1, w),
        leftPart(level-1, w-(1<<(level-1))),
        leftPart(level-1, w),
        leftPart(level-1, w-(1<<(level-1))),
        )

@cached
def topPart(level,w):
    if level == 0:
        if w <= 0:
            return zero
        return one
    return getQuad(
        topPart(level-1, w),
        topPart(level-1, w),
        topPart(level-1, w-(1<<(level-1))),
        topPart(level-1, w-(1<<(level-1))),
        )

def makeRect(level, x1, y1, x2, y2):
    l = leftPart(level, x1)
    r = leftPart(level, x2)
    t = topPart(level, y1)
    b = topPart(level, y2)
    
    return quadMap(lambda l,r,t,b: int(l==t==0 and r==b==1) ,l,r,t,b)
        
#q1 = getQuad(zero,one,one,zero)
#q2 = getQuad(q1,q1,full(1),q1)
#printCells(q2.aliveCells())
#printCells(evolve(q2,1).aliveCells())

#printQuad(quadMap(lambda x: 1-x, q2))

#printQuad(leftPart(4,6))

#printQuad(makeRect(3,1,2,3,4))

import sys
import re
import os
import time
from StringIO import StringIO
from itertools import *
from multiprocessing import Pool
from pprint import pprint
from bisect import bisect

#from hashlife import *

parallel = True

def read(caseNo):
    R = int(next(fin))
    rects = [map(int,next(fin).split()) for i in range(R)]
    return locals()

def solve(data):
    clearCache()
    print 'Case #{0}'.format(data.caseNo)

    rects = data.rects

    level = 8
    field = empty(level)

    for x1, y1, x2, y2 in rects:
        field = quadMap(max, field, makeRect(level,x1,y1,x2+1,y2+1))

    field = getQuad(empty(level), empty(level), empty(level), field)

    class Q(object):
        def __len__(self):
            return 1<<level
        def __getitem__(self, index):
            if evolve(field, index) == empty(level):
                return 1
            return 0

#    printQuad(field)

    out = StringIO()
    print>>out, bisect(Q(),0)
    return out.getvalue()

class DataObject(object):
    def __init__(self, d):
        self.__dict__.update(d)

        
def main():
    if len(sys.argv) != 2:
        print 'specify input file'
        exit()

    startTime = time.clock()

    global fin, fout
    fin = open(sys.argv[1])
    fout = open(os.path.splitext(sys.argv[1])[0]+'.out', 'w')

    numCases = int(next(fin))
    inputs = (DataObject(read(i)) for i in range(numCases))


    if parallel:
        pool = Pool(4)
        results = pool.imap(solve, inputs)
    else:
        results = imap(solve, inputs)

    for caseNo, result in enumerate(results):
        fout.write('Case #%s: '%(caseNo+1))
        fout.write(result)

    fin.close()
    fout.close()

    print 'it took %.1fs'%(time.clock()-startTime)

if __name__ == "__main__":
    main()