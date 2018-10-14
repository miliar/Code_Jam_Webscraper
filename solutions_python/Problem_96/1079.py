import string
f = open("B-large.in")
fwrite = open('B-large.out', 'w')
numCases = int(f.readline())
for i in range(0,numCases):
    numWorse = 0
    nextLine = f.readline()
    nextLineArray = nextLine.split(' ')
    nextLineArray = map(int,nextLineArray)
    numGooglers = int(nextLineArray[0])
    surprisingTriplets = int(nextLineArray[1])
    thresholdScore = int(nextLineArray[2])
    totals = nextLineArray[3:len(nextLineArray)]
    totals.sort()
    minimumUnsurprisingTotal = thresholdScore*3 - 2
    minimumSurprisingTotal = thresholdScore*3 - 4
    if(thresholdScore == 0):
        numWorse = 0
    elif(thresholdScore == 1):
        for j in totals:
            if( j == 0):
                numWorse += 1
    else:
        for j in totals:
            #see if bad enough without using the surprising count
            if(j < minimumUnsurprisingTotal):
                if (surprisingTriplets > 0):
                    if( j < minimumSurprisingTotal):
                        numWorse += 1
                    else:
                        surprisingTriplets -= 1
                else:
                    numWorse += 1
            else:
                break
   # print "Case #" + str(i+1) + ": " + f.readline().translate(trans)
    fwrite.write("Case #" + str(i+1) + ": " + str(len(totals) - numWorse) +'\n')
f.close()
fwrite.close()
