import numpy as np
import sys

#fin = sys.arg[1]
fin = "./A-large.in"

with open(fin) as f:
    lines = f.readlines()

for case, line in enumerate(lines[1:]):
    n, people = line.strip().split()

    n = int(n)
    people = map(int, people)

    ans = 0
    acc = 0
    for i, p in enumerate(people):
        if acc < i and p > 0:
            ans += (i - acc)
            acc += (i - acc)
        acc += p

    print "Case #%d: %d" % (case + 1, ans)





