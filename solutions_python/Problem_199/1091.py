import sys
import math

with open("../files/" + 'Q2017A'[-1] + "-large.in", 'r') as inp, open(
                    "../files/output" + 'Q2017A'[-1] + ".txt", 'w') as out:
    t = int(inp.readline())
    for i in xrange(t):
        string = "Case #" + str(i + 1) + ": {}"
        res = 0
        data, k = inp.readline().split()
        k = int(k)
        change = [False] * len(data)
        flips = 0
        for i in xrange(len(data)):
            happy = data[i] == '+'
            if happy != (flips % 2 == 0):
                if i >= len(data) - k + 1:
                    res = "IMPOSSIBLE"
                    break
                flips += 1
                res += 1
                change[i+k-1] = True
            if change[i]:
                flips -= 1
        out.write(string.format(res) + "\n")
