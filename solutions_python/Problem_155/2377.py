import numpy as np
import csv as csv

print 'Starting'

inFile = open('A-large.in','rb')
data = csv.reader(inFile,delimiter=' ')

outFile = open('A-large.out','w')

data.next()
count = 0
for row in data:
    numStanding = 0
    numFriends = 0
    maxShyness = int(row[0])
    shynessString = row[1]
    for i in xrange(maxShyness+1):
        if numStanding < i:
            numFriends += i - numStanding
            numStanding += i - numStanding
        numAtShyness = int(shynessString[i])
        numStanding += numAtShyness
        
    count += 1
    outLine = 'Case #' + str(count) + ': ' + str(numFriends)
    outFile.write(outLine)
    outFile.write('\n')

inFile.close()
outFile.close()


print 'Done'
