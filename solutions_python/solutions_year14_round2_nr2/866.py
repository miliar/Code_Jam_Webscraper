import itertools
import sys

def do_test_case(fd):

    (amax,bmax,kmax) = [int(x) for x in fd.readline().split()]

    wins = 0

    for a in itertools.count(1):
        av = a-1
        if av >= amax: 
            break
        for b in itertools.count(1):
            bv = b-1
            if bv >= bmax: 
                break
            if av&bv < kmax:
                wins += 1

    return wins


##################
file = sys.argv[1]

fd = open(file, 'r')

num_tests = fd.readline()

for i in xrange(1,int(num_tests)+1):
    x = do_test_case(fd)
    print "Case #%d: %d" % (i,x)

