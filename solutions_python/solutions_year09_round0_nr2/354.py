class GridPt (object):
    def __init__(self,y,x):
        self.y = y
        self.x = x
        self.path = {}
        self.path[hashPt(y,x)] = True
        self.active = True

    def moveTo(self,y,x):
        self.y = y
        self.x = x
        self.path[hashPt(y,x)] = True

    def mergePt(self, other):
        for coord in other.path.iterkeys():
            self.path[coord] = True

    def getCoords(self):
        return (self.y,self.x)

    def setCoords(self,coord):
        self.y = coord[0]
        self.x = coord[1]

    def setInactive(self):
        self.active = False

def hashPt(y,x):
    return str(y)+","+str(x)

class HeightGrid (object):
    #NOTE: COORDS ARE IN [Y][X]
    def __init__(self):
        self.gridArr = []
        self.basins = []
        self.rows = 0
        self.cols = 0

    def addRow(self, rowArr):
        self.gridArr.append([int(x) for x in rowArr])
        self.basins.append([-1 for x in rowArr])
        self.cols = len(rowArr)
        self.rows += 1
    
    def getLowestNeighbor(self,y,x):
        curVal = 1000000000000000
        curNeighbor = None
        if y-1 >= 0 and self.gridArr[y-1][x] < curVal: #N
            curNeighbor = (y-1,x)
            curVal = self.gridArr[y-1][x]
        if x-1 >= 0 and self.gridArr[y][x-1] < curVal: #W
            curNeighbor = (y,x-1)
            curVal = self.gridArr[y][x-1]
        if x+1 < self.cols and self.gridArr[y][x+1] < curVal: #E
            curNeighbor = (y,x+1)
            curVal = self.gridArr[y][x+1]
        if y+1 < self.rows and self.gridArr[y+1][x] < curVal: #S
            curNeighbor = (y+1,x)
            curVal = self.gridArr[y+1][x]

        return curNeighbor

    def colorBasins(self):

        activePts = self.cols * self.rows
        numEntities = self.cols * self.rows
        
        for j in range(0,len(self.gridArr)):
            for i in range(0,len(self.gridArr[j])):
                self.basins[j][i] = GridPt(j,i)


        while activePts > 0:
            for j in range(0,len(self.gridArr)):
                for i in range(0,len(self.gridArr[j])):
                    if self.basins[j][i] is not None:
                        curPt = self.basins[j][i]

                        curPtLoc = curPt.getCoords()
                        nextPtLoc = self.getLowestNeighbor(curPtLoc[0], curPtLoc[1])
                        if not nextPtLoc is None and self.gridArr[nextPtLoc[0]][nextPtLoc[1]] < self.gridArr[curPtLoc[0]][curPtLoc[1]]:
                            curPt.setCoords(nextPtLoc)
                            other = self.basins[nextPtLoc[0]][nextPtLoc[1]]
                            if other is not None:
                                activePts -= 1 #we're deleting the one that moved so we're guaranteed it was active
                                other.mergePt(curPt) #merge out curpt
                            else:
                                self.basins[nextPtLoc[0]][nextPtLoc[1]] = curPt
                            self.basins[curPtLoc[0]][curPtLoc[1]] = None #kill curpt either way
                        else:
                            if curPt.active:
                                activePts -= 1
                                curPt.setInactive()

        outPts = []

        for j in range(0,len(self.gridArr)):
            for i in range(0,len(self.gridArr[j])):
                if self.basins[j][i] is not None:
                    outPts.append(self.basins[j][i].path)
        return outPts

f = open('intext.txt')
of = open('out5.txt', 'w')
numTests = int(f.readline())
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(0,numTests):
    aIndex = 0
    grid = HeightGrid()
    dimLine = f.readline()
    numRows = int(dimLine.split(" ")[0])
    numCols = int(dimLine.split(" ")[1])
    for j in range(0,numRows):
        grid.addRow([int(x) for x in f.readline().split(" ")])
    groups = grid.colorBasins()
    of.write("Case #%s: \n" % str(i+1))
    print "now on test %d" % (i+1)
    for y in range(0, numRows):
        for x in range(0,numCols):
            for group in groups:
                if hashPt(y,x) in group:
                    if not "letter" in group:
                        group["letter"] = alphabet[aIndex]
                        aIndex += 1
                    of.write(group["letter"] + " ")
                    break
        of.write("\n")

of.flush()
of.close()
f.close()

                                                    
