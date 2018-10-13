import sys
import math

with open("../files/" + 'Q2017B'[-1] + "-large.in", 'r') as inp, open(
                    "../files/output" + 'Q2017B'[-1] + ".txt", 'w') as out:
    t = int(inp.readline())
    for i in xrange(t):
        string = "Case #" + str(i + 1) + ": {}"
        res = ""
        n = inp.readline().strip()
        if len(n) == 1:
            res = n
        repeat_start = None
        for i in xrange(len(n) - 1):
            cur = int(n[i])
            nxt = int(n[i+1])
            if cur < nxt:
                if repeat_start is not None:
                    repeated = n[repeat_start]
                    times = i + 1 - repeat_start
                    res += repeated * times
                    repeat_start = None
                else:
                    res += str(cur)
                if i == len(n) - 2:
                    res += str(nxt)
            elif cur > nxt:
                if repeat_start is not None:
                    first = int(n[repeat_start]) - 1
                    if first > 0:
                        res += str(first)
                    times = i - repeat_start
                    res += "9" * times
                elif cur > 1:
                    res += str(cur - 1)
                res += "9" * (len(n) - i - 1)
                break
            else:
                if repeat_start is None:
                    repeat_start = i
                if i == len(n) - 2:
                    repeated = n[repeat_start]
                    times = len(n) - repeat_start
                    res += repeated * times
        out.write(string.format(res) + "\n")
