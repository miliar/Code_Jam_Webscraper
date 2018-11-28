import sys

__author__ = 'David'


def solve(number):
    largest = number
    length = len(number)
    for i in xrange(length - 1):
        first = int(number[i])
        second = int(number[i + 1])

        if second < first:
            base_length = (length - i - 1)
            prefix = int(number[:i + 1]) - 1
            nines = '9' * base_length
            largest = solve((str(prefix) + nines).strip('0'))
            #print number, base_length, prefix, nines
            break
    return largest

T = int(sys.stdin.readline())

for t in xrange(T):
    N = sys.stdin.readline().strip()
    print "Case #%d: %s" % (t + 1, solve(N))
