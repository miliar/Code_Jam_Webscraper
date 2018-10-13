import sys
import math

with open("../files/" + '20171A'[-1] + "-large.in", 'r') as inp, open(
                    "../files/output" + '20171A'[-1] + ".txt", 'w') as out:
    t = int(inp.readline())
    for i in xrange(t):
        string = "Case #" + str(i + 1) + ":"
        res = 0
        n, m = map(int, inp.readline().split())
        data = []
        for j in xrange(n):
            data.append(list(inp.readline().strip()))

        for row in data:
            for k in xrange(m):
                if row[k] == '?':
                    continue
                cur = row[k]
                prev = k - 1
                while prev >= 0 and row[prev] == "?":
                    row[prev] = cur
                    prev -= 1
                after = k + 1
                while after < m and row[after] == "?":
                    row[after] = cur
                    after += 1
        for k in xrange(n):
            row = data[k]
            if row[0] == "?":
                continue
            prev = k - 1
            while prev >= 0 and data[prev][0] == "?":
                data[prev] = row[:]
                prev -= 1
            after = k + 1
            while after < n and data[after][0] == "?":
                data[after] = row[:]
                after += 1

        out.write(string + "\n")
        for row in data:
            out.write("".join(row) + "\n")
