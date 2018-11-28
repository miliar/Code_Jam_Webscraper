import sys

def calc_trees():
    """Read data from stdin and calculate all trees.

    Returns a list of coordinates (tuples of ints).

    """
    n,A,B,C,D,x,y,M = (int(e) for e in raw_input().split())
    trees = [(x, y)]
    for i in xrange(n - 1):
        x = (A * x + B) % M
        y = (C * y + D) % M
        trees.append((x, y))
    return trees

N = input()
for i in xrange(N):
    result = 0
    trees = calc_trees()
    i1 = 0
    for t1 in trees:
        i2 = i1 + 1
        for t2 in trees[i1 + 1:]:
            i3 = i2 + 1
            for t3 in trees[i2 + 1:]:
                x = (t1[0] + t2[0] + t3[0]) / 3.0
                y = (t1[1] + t2[1] + t3[1]) / 3.0
                if (x == int(x) and y == int(y)):
                    result += 1
                i3 += 1
            i2 += 1
        i1 += 1
    print "Case #%d: %d" % (i + 1, result)
