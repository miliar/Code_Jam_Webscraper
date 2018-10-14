import sys
import math
import re
import io

inputFile = sys.argv[1]
outFile = sys.argv[2]


class Q1:
    def __init__(self,file):
        line = file.readline().strip()
        arr = line.split(" ")
        rows = int(arr[0])
        cols = int(arr[1])
        self.results = []
        timesToEnter = 0
        for i in xrange(rows):
            line = file.readline().strip()
            numOfQs = line.count("?")
            if numOfQs<cols:
                firstCharIndex = re.search(r'[^?]', line).start()
                firstChar = line[firstCharIndex]
                lineStream = io.BytesIO()
                for j in xrange(len(line)):
                    if line[j]!=firstChar and line[j]!='?':
                        firstChar=line[j]
                    lineStream.write(firstChar)
                finalLine = lineStream.getvalue()
                lineStream.close()
                for j in xrange(timesToEnter + 1):
                    self.results.append(finalLine)
                    timesToEnter=0
            else:
                if(len(self.results)>0):
                    for j in xrange(timesToEnter+1):
                        self.results.append(self.results[len(self.results)-1])
                        timesToEnter = 0
                else: timesToEnter+=1


f = open(inputFile,"r")

firstLine = f.readline()
numberOfWords = int(firstLine)
print numberOfWords
o = open(outFile, "w")
i=0
for wordNumber in xrange(numberOfWords):
    i+=1
    d = Q1(f)
    print "Case #{0}:".format(i,)
    for row in d.results:
        print row

    o.write( "Case #{0}:\n".format(i))
    for row in d.results:
        o.write("{0}\n".format(row))

#    print "Case #{0}: {1}".format(gameNumber+1,g.getWinnerText())

#for line in f:
    #print line

#print inputFile
#print outFile