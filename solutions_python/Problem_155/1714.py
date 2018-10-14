import os
import sys


def solve(s):
    sum, diff = 0, 0
    for i in xrange(len(s)):
        if (i > sum):
            diff += (i - sum)
            sum = i
        sum += int(s[i])
    return diff


f = open(os.path.join(sys.path[0], 'A-large.in'))
out = open(os.path.join(sys.path[0], 'A-large.out'), 'w')

T = int(f.readline().strip())
for t in xrange(T):
    s_max, s = f.readline().strip().split()
    result = "Case #{0}: {1}".format(t + 1, solve(s))
    out.write(result + "\n")
    print result
out.close()