import sys

inputFile = sys.argv[1]

sys.stdin = open(inputFile,"r")

N = int(raw_input())

for i in xrange(N):
    inputline = raw_input().split()
    k = int(inputline[0])
    inputline = inputline[1:]

    orange = 1
    blue = 1
    time = 0

    curIndex = 0

    thisTime = 0
    firstMove = 0
    while curIndex < 2*k:
        curColor = inputline[curIndex]
#        print "firstMove is %c %d" % (curColor,int(inputline[curIndex+1]))
        if curColor == 'O':
            firstMove = abs(orange - int(inputline[curIndex+1]))
        else:
            firstMove = abs(blue - int(inputline[curIndex+1]))

        thisTime = -min(firstMove, thisTime)
#        print "subtracted %d (firstMove = %d)" % (thisTime, firstMove)

        while curIndex < 2*k and curColor == inputline[curIndex]:
            if curColor == 'O':
                thisTime += abs(orange - int(inputline[curIndex+1])) + 1
                orange = int(inputline[curIndex+1])
            else:
                thisTime += abs(blue - int(inputline[curIndex+1])) + 1
                blue = int(inputline[curIndex+1])
            curIndex += 2
        time += thisTime
#        print "took %d" % thisTime


    print "Case #%d: %d" % (i+1, time)
