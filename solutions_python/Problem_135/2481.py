#!/usr/bin/env python
import fileinput

def solve(r1, g1, r2, g2):
    l = [x for x in g1[r1-1] if x in g2[r2-1]]

    if len(l) == 0:
        return "Volunteer cheated!"
    if len(l) > 1:
        return "Bad magician!"
    return l[0]

def main():
    inp = fileinput.input()
    T = int(inp.next())

    for i in xrange(T):
        r1 = int(inp.next())
        g1 = [[int(x) for x in inp.next().split(' ')] for _ in xrange(4)]
        r2 = int(inp.next())
        g2 = [[int(x) for x in inp.next().split(' ')] for _ in xrange(4)]
        print "Case #%d: %s" % (i+1, solve(r1,g1,r2,g2))

if __name__ == '__main__':
    main()