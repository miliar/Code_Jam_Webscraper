
import sys

def debug(args):
    print >> sys.stderr, args

fin = sys.stdin
T = int(fin.readline())
for case in range(1, T + 1):
    D = int(fin.readline())
    diners = map(int, fin.readline().split())

    costs = []
    for i in range(1, 1002):
        cost = i
        for d in diners:
            cost += (d-1) / i
        costs.append(cost)

    best = min(costs)


    print "Case #%d: %s" % (case, best)