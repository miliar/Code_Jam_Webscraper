inf = open("a.in", "r")
ouf = open("a.out", "w")
T = int(inf.readline())
for t in xrange(T):
    print >> ouf, "Case #" + str(t + 1) + ":",
    parts = inf.readline().split()
    n = int(parts.pop(0))
    col = []
    num = []
    for i in xrange(len(parts)):
        if i % 2 == 0:
            col += [parts[i]]
        else:
            num += [int(parts[i])]
    x = 1
    y = 1
    res = 0
    for i in xrange(n):
        if col[i] == "O":
            nextX = num[i]
            diff = abs(nextX - x) + 1
            res += diff
            x = nextX

            j = i
            nextY = -1
            while (j < n):
                if (col[j] == "B"):
                    nextY = num[j]
                    break
                j += 1
            if nextY >= 0:
                if y <= nextY:
                    y = min(y + diff, nextY)
                else:
                    y = max(y - diff, nextY)
        else:
            nextY = num[i]
            diff = abs(nextY - y) + 1
            res += diff
            y = nextY

            j = i
            nextX = -1
            while (j < n):
                if (col[j] == "O"):
                    nextX = num[j]
                    break
                j += 1
            if nextX >= 0:
                if x <= nextX:
                    x = min(x + diff, nextX)
                else:
                    x = max(x - diff, nextX)
    print >> ouf, res
inf.close()
ouf.close()    

