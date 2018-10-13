import sys
import operator
with open(sys.argv[1]) as f:
    T = int(f.readline().strip())
    for i in range(T):
        print "Case #%d:" % (i+1),
        f.readline()
        ints = [int(x) for x in f.readline().strip().split()]
        if reduce(operator.xor, ints):
            print "NO"
        else:
            print sum(ints) - min(ints)
