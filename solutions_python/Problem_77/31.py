import sys

infile = sys.stdin

T = int(infile.readline())
for i in xrange(T):
    infile.readline() # ignore length
    values = list(map(int, infile.readline().split()))
    # EV is one per non-sorted item, so see how many are already sorted
    result = 0
    for a,b in zip(values, sorted(values)):
        if a!=b: result += 1
    
    print("Case #%d: %s" % (i+1, result))