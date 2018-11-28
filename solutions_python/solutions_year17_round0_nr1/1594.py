import csv as csv

print 'Starting'

inFile = open('A-large.in','rb')
##inFile = open('test.in','rb')
data = csv.reader(inFile,delimiter=' ')
numTests = int(data.next()[0])

outFile = open('outputSubmission.csv','wb')
outer = csv.writer(outFile)
##outString = 'Case #1:' 
##outer.writerow([outString])


def flipper(flipString):
    flippedString = ''
    for val in flipString:
        if val == '+':
            flippedString += '-'
        else:
            flippedString += '+'
    return flippedString


count = 0
for i in xrange(numTests):
    pString, flipperSize = data.next()
    pString = list(pString)
    flipperSize = int(flipperSize)
    flipCount = 0
    for j in xrange(len(pString)):
        #print pString
        if pString[j] == '-':
            if len(pString[j::]) < flipperSize:
                flipCount = 'IMPOSSIBLE'
            else:
                flipCount += 1
                pString[j:j+flipperSize] = flipper(pString[j:j+flipperSize])
            
    outString = 'Case #' + str(i+1) + ': ' + str(flipCount)
    #print outString
    outer.writerow([outString])
    count += 1


inFile.close()
outFile.close()
            
        

print 'Done'
