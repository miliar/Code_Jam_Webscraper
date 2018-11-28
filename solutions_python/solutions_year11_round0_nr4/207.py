import sys

num_cases = int(sys.stdin.readline())


def get_num_perms(Pi):
    ordered = range(1, len(Pi) + 1)
    diffs = [(a != b) for a, b in zip(Pi, ordered)]
    return diffs.count(True)


for j in xrange(num_cases):
    N = int(sys.stdin.readline().strip())
    Pi = [int(e) for e in sys.stdin.readline().split()]
    if N != len(Pi):
        raise Exception("input format error")
        
    print "Case #%s: %s" % (j+1, get_num_perms(Pi))
    j += 1
