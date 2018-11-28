memo = {}
def naive(sub, large):
    if not sub:
        return 1
    t = (sub, large)
    if t in memo:
        return memo[t] 
    tot = 0
    c = sub[0]
    rest = sub[1:] 
    for i in range(len(large)):
        if large[i] == c:
            tot = (tot + naive(rest, large[i+1:])) % 10000

    memo[t] = tot
    return tot

import sys

sys.stdin.readline()

i = 1
for line in sys.stdin:
    print "Case #%d: %04d" % (i, naive("welcome to code jam", line))
    i += 1
