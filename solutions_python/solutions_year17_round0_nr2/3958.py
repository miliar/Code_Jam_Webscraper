import sys

T = int(sys.stdin.readline())


def solve(x):
    first_j = -1

    for j in xrange(len(x)-1):
        if x[j] > x[j+1]:
            first_j = j
            break

    if first_j == -1:
        return x

    y = x[:first_j+1] + '0' * (len(x) - first_j - 1)
    return solve(str(int(y) - 1))


for i in xrange(T):
    x = sys.stdin.readline().strip()
    print 'Case #%d: %s' % (i+1, solve(x))
