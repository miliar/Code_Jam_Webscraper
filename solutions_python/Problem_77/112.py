import sys
fileName = 'gorosort_test'
f = open(fileName + '.in')
outFile = open(fileName +'.out', 'w')
def println(s):
    print >> outFile, s
    print s

testCases = int(f.readline())
for test in range(testCases):
    n = int(f.readline())
    values = [int(z) for z in f.readline().split()]
    z = values[:]
    z.sort()
    answer = n
    for a, b in zip(values, z):
        if a == b: answer -= 1
    println("Case #%d: %.6f" % (test + 1, answer))
