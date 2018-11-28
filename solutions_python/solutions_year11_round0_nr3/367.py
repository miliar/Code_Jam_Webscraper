import sys

def main():
    f = open(sys.argv[1])
    testCases = int(f.readline())
    for i in xrange(1, testCases + 1):
        noOfCandy = int(f.readline())
        cs = map(int, f.readline().split())
        print "Case #%d: %s" % (i, solve(cs))
    f.close()

def solve(cs):
    cs.sort()
    xors = reduce(lambda x, y: x ^ y, cs)
    if xors != 0:
        return "NO"
    else:
        return str(sum(cs) - cs[0])

main()
