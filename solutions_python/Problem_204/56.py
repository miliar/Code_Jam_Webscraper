import sys
import math

inputFile = sys.argv[1]
outFile = sys.argv[2]


class Q2:

    def findAMatch(self,theMin,theMax,ingredient):
        if(theMin>theMax): return False
        if(ingredient>len(self.options)-1): return True
        index = self.curIndices[ingredient]
        for i in xrange(index,self.packages):
            p = self.options[ingredient][i]
            newMin = max(theMin,p[1])
            newMax = min(theMax,p[2])
            if self.findAMatch(newMin,newMax,ingredient+1):
                self.curIndices[ingredient]=i+1
                return True
        return False



    def __init__(self,file):
        l = file.readline().strip()
        arr = l.split(" ")
        ingredients = int(arr[0])
        self.packages = int(arr[1])
        l2 = file.readline().strip()

        requirements = map(lambda x:int(x),l2.split(" "))
        vals = []
        for i in xrange(ingredients):
            amounts = map(lambda x:float(x)/requirements[i],file.readline().strip().split(" "))
            amounts.sort()
            amountsAndPackages = map(lambda x:
                                     (x,math.ceil(x/1.1),math.floor(x/0.9))
                                     ,amounts)
            vals.append(amountsAndPackages)
        self.options=vals
        self.result=0
        self.curIndices = []
        for i in xrange(len(vals)):
            self.curIndices.append(0)
        while(self.findAMatch(0,99999999,0)):
            self.result+=1


f = open(inputFile,"r")

firstLine = f.readline()
numberOfWords = int(firstLine)
print numberOfWords
o = open(outFile, "w")
i=0
for wordNumber in xrange(numberOfWords):
    i+=1
    d = Q2(f)
    print "Case #{0}: {1}".format(i,d.result)

    o.write( "Case #{0}: {1}\n".format(i,d.result))
#    print "Case #{0}: {1}".format(gameNumber+1,g.getWinnerText())

#for line in f:
    #print line

#print inputFile
#print outFile