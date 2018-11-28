__author__ = 'archeg'

class solveD():
    def __init__(self, naomisBlocks, kensBlocks, pattern):
        self.naomisBlocks = sorted(list(naomisBlocks))
        self.kensBlocks = sorted(list(kensBlocks))
        self.moveCounter = 0
        self.pattern = pattern

    def kensMove(self, toldNaomi):
        for i in range(len(self.kensBlocks)):
            if self.kensBlocks[i] > toldNaomi:
                toldKen = self.kensBlocks[i]
                self.kensBlocks.__delitem__(i)
                return toldKen

        j = len(self.kensBlocks) - 1
        kensChoice = self.kensBlocks[j]
        self.kensBlocks.__delitem__(j)
        return kensChoice
        #toldKen = self.kensBlocks[0]
        #self.kensBlocks.__delitem__(0)
        #return toldKen

    def naomiStraightMove(self):
        if len(self.naomisBlocks) == 0:
            return None
        toldNomi = self.naomisBlocks[0]
        self.naomisBlocks.__delitem__(0)
        return toldNomi

    def naomiDeceighfulMove(self):
        if len(self.naomisBlocks) == 0:
            return (None, None)

        def doDeceigh():
            naomiMove = self.naomisBlocks[0]
            self.naomisBlocks.__delitem__(0)

            kensBlockToGo = self.kensBlocks[len(self.kensBlocks) - 1]
            return (naomiMove, kensBlockToGo - .00000001)

        def doStraight():
            indexToPlay = len(self.naomisBlocks) - 1
            naomiMove = self.naomisBlocks[indexToPlay]
            self.naomisBlocks.__delitem__(indexToPlay)
            return (naomiMove, naomiMove)

        #print self.naomisBlocks
        #print self.kensBlocks
        self.moveCounter += 1
        #if self.pattern[self.moveCounter]:
        #    return doDeceigh()
        #else:
        #    return doStraight()
        if max(self.kensBlocks) < max(self.naomisBlocks):
            return doStraight()
        return doDeceigh()
        #
        #if max(self.kensBlocks) < max(self.naomisBlocks):
        #    return doStraight()
        #else:
        #    return doDeceigh()


    def computeStraight(self):
        naomiScore = 0
        while True:
            naomiMove = self.naomiStraightMove()
            if not naomiMove:
                return naomiScore

            kensMove = self.kensMove(naomiMove)
            if naomiMove > kensMove:
                naomiScore += 1

    def computeDeceiful(self):

        naomiScore = 0
        while True:
            naomiMove, naomiTold = self.naomiDeceighfulMove()
            if not naomiMove:
                return naomiScore

            kensMove = self.kensMove(naomiTold)

            #if (naomiTold == naomiMove):
            #    print "+ %s %s %s" % (naomiMove, naomiTold, kensMove)
            #else:
            #    print "- %s %s %s" % (naomiMove, naomiTold, kensMove)
            if (naomiMove > kensMove) != (naomiTold > kensMove):
                print "Error"

            if naomiMove > kensMove:
                naomiScore += 1

def Run(fileName, runOnly = None, pattern = None):
    def readArray(f):
        return [float(x) for x in f.readline().split(' ')]

    def outputMatrix(lines, matrix):
        for line in matrix:
            lines.append("".join(line) + "\n")

    outputLines = []
    with open(fileName, 'r') as fi:
        runs = int(fi.readline())
        for i in range(1, runs + 1):
            arrLength = int(fi.readline())
            naomisBlocks = readArray(fi)
            kensBlocks = readArray(fi)
            if not runOnly or i in runOnly:
                warScore = solveD(naomisBlocks, kensBlocks, pattern).computeStraight()
                deceifulScore = solveD(naomisBlocks, kensBlocks, pattern).computeDeceiful()
                if deceifulScore == 6:
                    print "-----------------------------------------------------------------"
                outputLines.append("Case #%i: %i %i\n" % (i, deceifulScore, warScore))

    #print "--------------"
    #for line in outputLines:
    #    print line
    with open("output.txt", 'w') as fo:
        fo.writelines(outputLines)


Run("input.txt")