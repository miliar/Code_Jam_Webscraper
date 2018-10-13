
def process(tc, smax, sarr):
    numStanding = int(sarr[0])
    numNeeded = 0
    totalNumNeeded = 0
    i = 0
    for elem in sarr[1:]:
        i += 1
        x = int(elem)
        numNeeded = 0
        if i > numStanding:
            numNeeded = i-numStanding

        numStanding += x + numNeeded
        totalNumNeeded += numNeeded
    print "Case #%d: %d" % (tc, totalNumNeeded)


lines = [line.strip() for line in open('A-large.in')]

n = int(lines[0])
for i in range(0, n):
    arr = lines[i+1].split(' ')
    sMax = int(arr[0])
    process(i+1, sMax, arr[1])

