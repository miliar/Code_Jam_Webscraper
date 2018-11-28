import math

fin = open("input.txt", "r")

tests_num = int(fin.readline())

for i in xrange(tests_num):
    [n, k] = [int(x) for x in fin.readline().split(" ")]

    pancakes = []
    for _ in xrange(n):
        pancakes.append([int(x) for x in fin.readline().split(" ")])
        r = pancakes[-1][0]
        h = pancakes[-1][1]
        pancakes[-1][0] = math.pi * r * r
        pancakes[-1][1] = 2 * math.pi * r * h

    pancakes.sort(key=lambda x: -x[1])
    best = -1
    for ii in xrange(n):
        cur = pancakes[ii][0] + pancakes[ii][1]
        num = 1
        for jj in xrange(n):
            if num == k:
                break
            if jj != ii and pancakes[ii][0] >= pancakes[jj][0]:
                num += 1
                cur += pancakes[jj][1]
        if num == k and cur > best:
            best = cur

    print "Case #" + str(i + 1) + ": " + str(best)


fin.close()