from math import pi

def pancakes(n, k):
    cakes = []
    for i in xrange(n):
        cakes.append([int(s) for s in raw_input().split(' ')])
    for x in cakes:
        x.append(2*pi*x[0]*x[1])
    cakes.sort(key = lambda x: x[2])
    bestSides = cakes[-k:]
    totSides = sum(x[2] for x in bestSides)
    bestRad = max(x[0] for x in bestSides)
    sa = totSides + pi*bestRad*bestRad
    others = list(filter(lambda x: x[0] > bestRad, cakes))
    for x in others:
        newBest = totSides - bestSides[0][2] + x[2] + pi*x[0]*x[0]
        sa = max(sa, newBest)
    return sa

def cores(n, k, u):
    probs = [float(s) for s in raw_input().split(" ")]
    probs.sort()
    num = 1
    while u > 0 and num < len(probs):
        x = probs[num] - probs[num - 1]
        for i in xrange(num):
            probs[i] += min(x, u / num)
        u -= x * num
        num += 1
    if u > 0:
        x = u / len(probs)
        for i in xrange(len(probs)):
            probs[i] += x
    result = 1
    for i in xrange(len(probs)):
        result *= probs[i]
    return min(result, 1)


def switching(ac, aj):
    c = []
    j = []
    for i in xrange(ac):
        c.append([int(s) for s in raw_input().split(' ')])
    for i in xrange(aj):
        j.append([int(s) for s in raw_input().split(' ')])
    c.sort(key= lambda x: x[0])
    j.sort(key=lambda x: x[0])
    lc = len(c)
    lj = len(j)
    if lc == lj == 0:
        return 2
    if lc == 1 and lj == 0:
        return 2
    if lc == 0 and lj == 1:
        return 2
    if lc == lj == 1:
        return 2
    if lc == 2:
        if c[1][0] - c[0][1] >= 720 or c[1][1] - c[0][0] <= 720:
            return 2
        return 4
    if lj == 2:
        if j[1][0] - j[0][1] >= 720 or j[1][1] - j[0][0] <= 720:
            return 2
        return 4

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
#t = int(input())  # read a line with a single integer
#for i in range(1, t + 1):
#    n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
#    print("Case #{}: {} {}".format(i, n + m, n * m))
    # check out .format's specification for more formatting options

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
#    u = float(raw_input())
    print "Case #{}: {}".format(i, switching(n, k))
    # check out .format's specification for more formatting options