import sys

def readline():
    return map(int, sys.stdin.readline().strip().split())

def mCol(world, col, val):
    for i in xrange(len(world)):
        if world [i][col] != val:
            return False
    for i in xrange(len(world)):
        world[i].pop(col)
        if len(world[i]) == 0:
            world.pop(i)
    return True

def mRow(world, row, val):
    for i in xrange(len(world[0])):
        if world[row][i] != val :
            return False
    world.pop(row)
    return True

def minWorld(w):
    m = 100
    for i in xrange(len(w)):
        for j in xrange(len(w[0])):
            if w[i][j] < m :
                m = w[i][j]
    return m

def getSize(w):
    if len(w) == 0: return 0, 0
    return (len(w), len(w[0]))

def cutExists(w, val):
    for i in xrange(len(w)):
        if mRow(w, i, val):
            return True
    for i in xrange(len(w[0])):
        if mCol(w, i, val):
            return True        
    return False

def solve(w):
    m, n = getSize(w)
    while m != 0 and n != 0:
        lowest = minWorld(w)
        if not cutExists(w, lowest):
            return "NO"
        m, n = getSize(w)
        if m == 1 or n == 1:
            return "YES"
    return "YES"
    
T = int(sys.stdin.readline())
for t in xrange(1, T+1):
    m, n = readline()
    world = [readline() for _ in xrange(m)]
    visited = [[0 for _ in xrange(n)] for _ in xrange(m)]
    if m == 1 or n == 1:
        print "Case #%d: YES" % t
        continue
    print "Case #%d: %s" %(t,solve(world))
