import sys
import io

inputFile = sys.argv[1]
outFile = sys.argv[2]


class Stalls:
    def __init__(self,file):
        defs = file.readline().strip()
        arr = defs.split(" ")
        self.stalls = long(arr[0])
        self.people = long(arr[1])

        self.currentStalls = [(self.stalls,1)]
        while self.people>0:
            currentSplit = self.currentStalls[0]
            currentLength = currentSplit[0]
            amount = currentSplit[1]
            first=-1
            second=-1
            del(self.currentStalls[0])
            if (currentLength%2==0):
                first = currentLength/2
                second = currentLength/2 - 1
            else:
                first=(currentLength-1)/2
                second=(currentLength-1)/2
            firstAdded=False
            secondAdded=False
            for index, item in enumerate(self.currentStalls):
                itemAmount = item[1]
                if (item[0]==first):
                    self.currentStalls[index]=(first,itemAmount+amount)
                    itemAmount+=amount
                    firstAdded=True
                if (item[0] == second):
                    self.currentStalls[index] = (second, itemAmount + amount)
                    secondAdded=True
            if (first!=second): #Should have simply splitted them in the first place
                if(not firstAdded) and (first>0):
                    self.currentStalls.append((first,amount))
                if (not secondAdded) and (second>0):
                    self.currentStalls.append((second, amount))
            elif(not firstAdded) and (first>0):
                self.currentStalls.append((first, 2*amount))

            self.result=(first,second)
            self.people-=amount

f = open(inputFile,"r")

firstLine = f.readline()
numberOfWords = int(firstLine)
print numberOfWords
o = open(outFile, "w")
i=0
for wordNumber in xrange(numberOfWords):
    i+=1
    d = Stalls(f)
    print "Case #{0}: {1} {2}".format(i,d.result[0],d.result[1])

    o.write( "Case #{0}: {1} {2}\n".format(i,d.result[0],d.result[1]))