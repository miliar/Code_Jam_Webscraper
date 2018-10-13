import sys

def solve(g1, l1, g2, l2):
    possib1 = set(l1[g1-1])
    possib2 = set(l2[g2-1])
    return possib1.intersection(possib2)


for tc in range(1, 1+int(raw_input())):
    g1 = int(raw_input())
    l1 = []
    for i in xrange(4):
        line = sys.stdin.readline()
        l1.append(map(int, line.split(" ")))
    g2 = int(raw_input())
    l2 = []
    for i in xrange(4):
        line = sys.stdin.readline()
        l2.append(map(int, line.split(" ")))
    r = solve(g1, l1, g2, l2)
    if len(r) == 1:
        print "Case #%d: %d" % (tc, list(r)[0])
    elif len(r) == 0:
        print "Case #%d: Volunteer cheated!" % tc
    else:
        print "Case #%d: Bad magician!" % tc


