import csv as csv
import numpy as np
import math

print 'Starting'

##inFile = open('B-large.in','rb')
inFile = open('C-small-2-attempt0.in','rb')
##inFile = open('test.in','rb')
data = csv.reader(inFile,delimiter=' ')
numTests = int(data.next()[0])

outFile = open('outputSubmission.csv','wb')
outer = csv.writer(outFile)
##outString = 'Case #1:' 
##outer.writerow([outString])



count = 0
for i in xrange(numTests):
    N,K = data.next()
    N = long(N)
    K = long(K)

    b = int(math.floor(np.log2(K)+0.0000000001))
    b = 2**b
    k = b-1
    r = K-k

    pastBinSize = (N-k)/(b)
    numPastBigBins = (N-k)%(b)

##    print k, r
##    print pastBinSize, numPastBigBins
    
    if r == 0 and numPastBigBins > 0:
        print 'This one'
        minSize = math.floor((pastBinSize+1))
        maxSize = math.ceil((pastBinSize-1))
    elif r == 0 and numPastBigBins == 0:
        print 'Or This one'
        minSize = math.floor(pastBinSize)
        maxSize = math.ceil(pastBinSize)
    if r <= numPastBigBins:
        minSize = math.floor(pastBinSize/2.)
        maxSize = math.ceil(pastBinSize/2.)
    elif r > numPastBigBins:
        minSize = math.floor((pastBinSize-1)/2.)
        maxSize = math.ceil((pastBinSize-1)/2.)

    outString = 'Case #' + str(i+1) + ': ' + str(int(maxSize)) + ' ' + str(int(minSize))
    outer.writerow([outString])
    print outString
    print ''
    count += 1
    #print count    


inFile.close()
outFile.close()
            
        

print 'Done'
