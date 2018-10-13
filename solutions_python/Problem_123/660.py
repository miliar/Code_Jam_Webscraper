import sys

DEBUG = False
MAX = 10

def solve(size, motes, operation):
    if len(motes) == 0:
        return operation

    result = []

    if size > motes[0]:
        if DEBUG:
            print size, operation, motes
            print 'pass', size + motes[0]
        result.append( solve(size + motes[0], motes[1:], operation) )

    if DEBUG:
        print size, operation, motes
        print 'remove operation', size
    result.append( solve(size, motes[1:], operation + 1) )

    if operation + 1 < MAX and len(motes) > 1:
        if DEBUG:
            print size, operation, motes
            print 'add operation', size + size - 1
        result.append( solve(size + size - 1, motes, operation + 1) )

    if DEBUG:
        print 'result : ' + str(result)
    return min(result)

for tc in xrange(1, int(sys.stdin.readline())+1):
    A, N = [int(w) for w in sys.stdin.readline().split()]
    other_motes = [int(w) for w in sys.stdin.readline().split()]
    other_motes.sort()

    result = solve(A, other_motes, 0)

    print 'Case #%d: %d' % (tc, result)
