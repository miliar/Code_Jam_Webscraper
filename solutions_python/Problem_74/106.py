import sys
fileName = 'bottrust_test'
f = open(fileName + '.in')
outFile = open(fileName +'.out', 'w')
def println(s):
    print >> outFile, s
    print s

testCases = int(f.readline())
for ta in range(testCases):
    data = f.readline().split()
    n = int(data[0])
    locO, timeO, locB, timeB = 1, 0, 1, 0
    lastTime = 0
    for i in range(n):
        bot = data[1+2*i]
        target = int(data[1+2*i+1])
        if bot == 'O':
            t = max(timeO + abs(target - locO) + 1, lastTime + 1)
            timeO = t
            locO = target
        else:
            t = max(timeB + abs(target - locB) + 1, lastTime + 1)
            timeB = t
            locB = target
        lastTime = t
    println("Case #%d: %d" % (ta + 1, lastTime))
        
