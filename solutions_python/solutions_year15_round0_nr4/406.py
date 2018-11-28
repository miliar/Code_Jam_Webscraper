import sys, os, pdb

sys.setrecursionlimit(5000)

#infile = open('input')
infile = sys.stdin

def read_array(vtype):
    line = infile.readline()
    return [vtype(v) for v in line.split(' ')]

def solve(x, r, c):
    G = 'GABRIEL'
    R = 'RICHARD'
    if x == 1:
        return G
    if x == 2:
        return G if (r % 2 == 0 or c % 2 == 0) else R

    if max(r, c) < x or min(r, c) < 2:
        return R

    if x == 3:
        if (r == 4 and c == 4) or (r == 2 and c == 4):
            return R
        else:
            return G

    if x == 4:
        return R if (r == 2 and c == 4) else G

if __name__ == '__main__':
    T = int(infile.readline())
    for case in xrange(T):
        x, r, c = read_array(int)
        if c < r:
            r, c = c, r
        ans = solve(x, r, c)
        print 'Case #%d: %s' % (case + 1, ans)
            
            
