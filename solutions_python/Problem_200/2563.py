from itertools import combinations_with_replacement
from bisect import bisect_right
digits = "123456789"
stuff = []
for r in range(1,19):
    for c in combinations_with_replacement(digits, r):
        stuff.append(int("".join(c)))


data = iter(open("B-large.in").read().splitlines())
T = int(next(data))
for caseNum in range(1, T + 1):
    n = int(next(data))
    i = bisect_right(stuff, n)
    print "Case #%d: %d" % (caseNum, stuff[i-1])