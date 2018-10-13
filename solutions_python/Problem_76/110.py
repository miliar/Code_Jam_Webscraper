import sys
fileName = 'candysplitting_test'
f = open(fileName + '.in')
outFile = open(fileName +'.out', 'w')
def println(s):
    print >> outFile, s
    print s

testCases = int(f.readline())
for t in range(testCases):
    n = int(f.readline())
    values = [int(a) for a in f.readline().split()]
    xorSum = reduce(lambda x,y: x ^ y, values)
    if xorSum != 0: println("Case #%d: NO" % (t+1))
    else: println("Case #%d: %d" % (t + 1, sum(values) - min(values)))