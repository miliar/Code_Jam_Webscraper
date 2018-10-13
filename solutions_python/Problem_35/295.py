def nextChar(char):
    return chr(ord(char) + 1)

class AltMap:
    def __init__(self, cellList, outputList):
        self.cl = cellList
        self.ol = outputList
        self.h = len(self.cl)
        self.w = len(self.cl[0])

    def north(self, r, c):
       return r-1, c

    def west(self, r, c):
       return r, c-1

    def east(self, r, c):
       return r, c+1

    def south(self, r, c):
       return r+1, c

    def getCell(self, r, c):
        if r > -1 and r < self.h and c > -1 and c < self.w:
            return self.cl[r][c]
        else:
            return None

    def getBasinName(self, r, c):
        if r > -1 and r < self.h and c > -1 and c < self.w:
            return self.ol[r][c]
        else:
            return None

    def setBasinName(self, r, c, name):
        if r > -1 and r < self.h and c > -1 and c < self.w:
            self.ol[r][c] = name
            return self.ol[r][c]

    def isSink(self, r, c):
        sink = True
        cellVal = self.getCell(r, c)
        n, w, e, s = self.getNeighbors(r, c)
        
        if n != None and n < cellVal:
            sink = False
        if w != None and w < cellVal:
            sink = False
        if e != None and e < cellVal:
            sink = False
        if s != None and s < cellVal:
            sink = False
            
        return sink

    def getFlowNeighbor(self, r, c):
        cellVal = self.getCell(r, c)
        n, w, e, s = self.getNeighbors(r, c)
        vl = [n, w, e, s]
        nvl = []
        for v in vl:
            if v != None:
                nvl.append(v)
        least = min(nvl)
        if least < cellVal:
            #flow
            if n == least:
                return self.north(r, c)
            if w == least:
                return self.west(r, c)
            if e == least:
                return self.east(r, c)
            if s == least:
                return self.south(r, c)
        else:
            return None
        
    def hasName(self, r, c):
        if self.getBasinName(r, c) == None:
            return False
        return True

    def flowFromCell(self, flowPath, r, c):
        flowPath.append((r,c))
        #print "r = " + str(r) + " c = " + str(c) + " Sink = " + str(self.isSink(r,c))
        if self.isSink(r,c):
            #print flowPath
            return flowPath
        else:
            r1, c1 = self.getFlowNeighbor(r, c)
            return self.flowFromCell(flowPath, r1, c1)
            

    def getNeighbors(self, r, c):
        nr, nc = self.north(r,c)
        wr, wc = self.west(r,c)
        er, ec = self.east(r,c)
        sr, sc = self.south(r,c)
        n = self.getCell(nr, nc)
        w = self.getCell(wr, wc)
        e = self.getCell(er, ec)
        s = self.getCell(sr, sc)
        return n, w, e, s

class Watersheds:
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile

        self.inf = open(infile, "r")
        self.outf = open(outfile, "w")
        self.readAndCompute()
        self.inf.close()
        self.outf.close()

    def readAndCompute(self):
        #first line
        firstline = self.inf.readline()
        self.T = int(firstline)

        self.maps = []
        for i in range(self.T):
            self.outf.write("Case #" + str(i+1) + ":\n")
            basinMap = self.readAndComputeMap()
            for row in basinMap:
                cc = 0
                for cell in row:
                    cc = cc + 1
                    if cc == len(row):
                        self.outf.write(cell)
                    else:
                        self.outf.write(cell + " ")
                self.outf.write("\n")

    def readAndComputeMap(self):
        #firstline of map H & W
        firstline = self.inf.readline()
        flw = firstline.split()
        H = int(flw[0])
        W = int(flw[1])

        #map
        inputMap = []
        for i in range(H):
            row = []
            rowLine = self.inf.readline()
            rw = rowLine.split()
            for r in rw:
                row.append(int(r))
            inputMap.append(row)
        #print inputMap

        #compute output map
        outputMap = []
        for i in range(H):
            outputMap.append([])
            for j in range(W):
                outputMap[i].append(None)

        amap = AltMap(inputMap, outputMap)
                
        currentChar = 'a'
        for i in range(H):
            for j in range(W):
               #print "i = " + str(i) + " j = " + str(j)
               flow = amap.flowFromCell([], i, j)
               name = None
               for fl in flow:
                   r, c = fl
                   if amap.hasName(r, c):
                       name = amap.getBasinName(r, c)
                       break
               if name == None:
                   name = currentChar
                   currentChar = nextChar(currentChar)
               for fl in flow:
                   r, c = fl
                   amap.setBasinName(r, c, name)
               #print "Flow Basin Name = " + name  
        #print amap.ol
        return amap.ol
        
if __name__ == "__main__":
    #al = Watersheds("in.txt", "out.txt")
    #asmall = Watersheds("B-small-attempt0.in", "B-small-attempt0.out")
    alarge = Watersheds("B-large.in", "B-large.out")
