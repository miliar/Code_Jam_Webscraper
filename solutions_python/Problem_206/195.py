import sys
import math

with open("../files/" + '20172A'[-1] + "-large.in", 'r') as inp, open(
                    "../files/output" + '20172A'[-1] + ".txt", 'w') as out:
    t = int(inp.readline())
    for i in xrange(t):
        string = "Case #" + str(i + 1) + ": {0:.6f}"
        d, n = map(int, inp.readline().split())
        max_t = 0
        for i in xrange(n):
            k, s = map(int, inp.readline().split())
            t = (d - k) * 1.0 / s
            max_t = max(max_t, t)
        res = d / max_t
        out.write(string.format(res) + "\n")
