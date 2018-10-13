import sys

num_cases = int(sys.stdin.readline())


def cheat_pat(Ci):
    xor_sum = reduce(lambda x, y: x^y, Ci, 0)
    if xor_sum:
        return 'NO'
    else:
        min_e = min(Ci)
        Ci.remove(min_e)
        return sum(Ci)


for j in xrange(num_cases):
    N = int(sys.stdin.readline().strip())
    Ci = [int(e) for e in sys.stdin.readline().split()]
    if N != len(Ci):
        raise Exception("input format error")
        
    print "Case #%s: %s" % (j+1, cheat_pat(Ci))
    j += 1
