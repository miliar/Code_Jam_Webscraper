from __future__ import division

def rins():
    return raw_input().strip()

IMPOSSIBLE = object()

def solve_next():
    r, c = [int(x) for x in rins().split()]
    tiles = [list(rins()) for i in xrange(r)]
    for row in xrange(r):
        for col in xrange(c):
            if tiles[row][col]==".":
                continue
            if tiles[row][col]=="#":
                if col==c-1 or row==r-1:
                    return IMPOSSIBLE
                if tiles[row+1][col]!="#":
                    return IMPOSSIBLE
                if tiles[row][col+1]!="#":
                    return IMPOSSIBLE
                if tiles[row+1][col+1]!="#":
                    return IMPOSSIBLE
                tiles[row][col]="/"
                tiles[row+1][col]="\\"
                tiles[row][col+1]="\\"
                tiles[row+1][col+1]="/"
    return "\n".join("".join(line) for line in tiles)

def run():
    t = int(rins())
    for i in xrange(t):
        print "Case #{0}:".format(i+1)
        result = solve_next()
        if result == IMPOSSIBLE:
            print "Impossible"
        else:
            print result

run()
