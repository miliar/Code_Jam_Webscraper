import sys

def run(R, k, queue):
    income = 0
    for r in xrange(R):
        sum = 0
        for i, elt in enumerate(queue):
            newsum = sum + elt
            if newsum > k:
                break
            sum = newsum
        income += sum
        queue = queue[i:] + queue[:i]
    return income

T = int(sys.stdin.readline())
for case in xrange(1, T+1):
    R, k, N = map(int, sys.stdin.readline().strip().split(" "))
    queue = map(int, sys.stdin.readline().strip().split(" "))
    assert N == len(queue)
    print "Case #%d: %s" % (case, run(R, k, queue))
