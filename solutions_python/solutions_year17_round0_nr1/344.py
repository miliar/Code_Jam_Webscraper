import sys
import math
from Queue import Queue

inputFile = sys.argv[1]
outFile = sys.argv[2]


class Pancakes:
    def __init__(self,file):
        pancakesLine = file.readline().strip()
        arr = pancakesLine.split(" ")
        self.pancakes = arr[0]
        self.flipper=int(arr[1])
        self.isFlipped=False
        self.flips = Queue()
        self.currentPancake=0
        self.totalFlips = 0
        self.nextFlip=-1

        while self.currentPancake<len(self.pancakes):
            if (self.currentPancake > self.nextFlip) and (not self.flips.empty()):
                self.nextFlip = self.flips.get()
            if (self.currentPancake==self.nextFlip):
                self.isFlipped = not self.isFlipped
            if(not self.isFaceup()):
                if(self.flippingAllowed()):
                    self.flip()
                else:
                    self.result="IMPOSSIBLE"
                    return
            self.currentPancake += 1

        self.result=self.totalFlips

    def flip(self):
        self.isFlipped = not self.isFlipped
        self.flips.put(self.currentPancake+self.flipper)
        self.totalFlips += 1
    def flippingAllowed(self):
        return self.currentPancake+self.flipper<=len(self.pancakes)
    def isFaceup(self):
        currentPancake = self.pancakes[self.currentPancake]
        return currentPancake==('-' if self.isFlipped else '+')



f = open(inputFile,"r")

firstLine = f.readline()
numberOfWords = int(firstLine)
print numberOfWords
o = open(outFile, "w")
i=0
for wordNumber in xrange(numberOfWords):
    i+=1
    d = Pancakes(f)
    print "Case #{0}: {1}".format(i,d.result)

    o.write( "Case #{0}: {1}\n".format(i,d.result))
#    print "Case #{0}: {1}".format(gameNumber+1,g.getWinnerText())

#for line in f:
    #print line

#print inputFile
#print outFile