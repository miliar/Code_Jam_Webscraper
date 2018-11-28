import sys

f = open(sys.argv[1])
fout = open(sys.argv[2], "w")

rl = lambda: f.readline().strip()
ra = lambda type: map(type, rl().split())
ri = lambda: int(rl())

def solve(a, R, C):
    for j in xrange(R):
        for i in xrange(C):
            if a[j][i] == '#':
                a[j][i] = '/'
                if i+1 == C or a[j][i+1] != '#': return False
                a[j][i+1] = '\\'
                if j+1 == R or a[j+1][i] != '#': return False
                a[j+1][i] = '\\'
                if a[j+1][i+1] != '#': return False
                a[j+1][i+1] = '/'
    return True

T = ri()
for t in xrange(T):
    R, C = ra(int)
    a = [[c for c in rl()] for j in xrange(R)]
    
    print >>fout, "Case #%d:" % (t+1)
    
    if solve(a, R, C):
        for j in xrange(R):
            print >>fout, "".join(a[j])
    else:
        print >>fout, "Impossible"
