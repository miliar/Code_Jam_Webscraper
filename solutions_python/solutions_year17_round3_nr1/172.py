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
    probs = [int(10000 * float(s)) for s in raw_input().split(" ")]
    OPT = {}
    for i in range(u + 1):
        OPT[0,i] = 1
    for i in range(1, n + 1):
        for j in range(u + 1):
            best = 0
            for x in range(j + 1):
                best = max(best, min(10000, probs[i] + x) * OPT[i - 1, j - x])
            OPT[i,j] = best
    return OPT[n,u]

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
    print "Case #{}: {}".format(i, pancakes(n, k))
    # check out .format's specification for more formatting options