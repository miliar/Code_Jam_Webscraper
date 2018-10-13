import math

f = open("B-large.in", 'r')

numTest = int(f.readline())
thisMax = 1


def relax(n):
    if (n < thisMax):
        return 0
    else:
        times = float(n) / thisMax - 1
        return int(math.ceil(times))




for x in xrange(numTest):
    n = int(f.readline())
    cakes = f.readline().split(" ")
    cakes = map(lambda x: int(x), cakes)
    Max = max(cakes);
    ways = []
    for i in xrange(Max):
        thisMax = i + 1
        times = reduce(lambda x,y: x + y, map(relax, cakes))
        ways.append(thisMax + times)

    run = min(ways)
    print "Case #" + str(x+1) + ": " + str(run)
