
class r:
    def __init__(self):
        pass

    def init(self, iLstTar):
        self.LstTar = iLstTar
        self.Pos = 1
        self.IdxTar = 0
        self.IdxTarReal = -1
        self.IdxTarCur = -1

    def doTar(self, iIdxTarCur):
        vDone = False
        if self.LstTar[iIdxTarCur][0] is self:
            # task for this robot
            # Test position
            if self.LstTar[iIdxTarCur][1] == self.Pos:
#                print 'Push button %d' % self.Pos,
                return True
            elif self.LstTar[iIdxTarCur][1] > self.Pos:
                self.Pos += 1
#                print 'Move to button %d' % self.Pos,
                return False
            else:
                self.Pos -= 1
#                print 'Move to button %d' % self.Pos,
                return False
        else:
            vDoneAction = False
            vIdx = iIdxTarCur+1
            # Search next task
            while vIdx < len(self.LstTar):
                if self.LstTar[vIdx][0] is self:
                    break
                vIdx += 1
            
            if vIdx < len(self.LstTar):
                # if task found test position and move to it if necessary
                if self.LstTar[vIdx][1] > self.Pos:
                    self.Pos += 1
#                    print 'Move to button %d' % self.Pos,
                    return True
                elif self.LstTar[vIdx][1] < self.Pos:
                    self.Pos -= 1
#                    print 'Move to button %d' % self.Pos,
                    return True
            
#            if not vDoneAction:
#                print 'Stay at button %d' % self.Pos,
            return True
            
        

class Prob:
    def __init__(self):
        self.dicR = {'O': r(), 'B': r()}
        self.LstCases = []
        self.ResCases = []
        pass

    def init(self, iFileName):
        self.FileName = iFileName
        pass

    def readFile(self):
        vf = open(self.FileName, 'r')
        try:
            # N. Test cases
            self.T = int(vf.readline())
            for vT in range(self.T):
                vLn = vf.readline()
                vLst = vLn.split()
                vLstTar = []
                for vN in range(int(vLst[0])):
                    vR = self.dicR[vLst[vN*2+1]]
                    vPos = int(vLst[vN*2+2])
                    vLstTar.append([vR, vPos])
                self.LstCases.append(vLstTar)
            vf.close()
        except:
            vf.close()
            raise

    def procCase(self, iLstTar):
        # init Robot
        for vR in self.dicR:
            self.dicR[vR].init(iLstTar)

        # do all tars
        vNT = 0
        for vIdxTar in range(len(iLstTar)):
            vTarNDone = False
            while not vTarNDone:
                vNT += 1
                vTarNDone = True
                # init Robot
#                print "%d: " % (vNT,),
                for vR in self.dicR:
#                    print vR,
                    vRes = self.dicR[vR].doTar(vIdxTar)
                    vTarNDone = vTarNDone and vRes
#                print
        return vNT
        pass
    
    def procCases(self):
        vN=0
        for v in self.LstCases:
            vN += 1
            print "Case #%d" % vN
            self.ResCases.append(self.procCase(v))

    def writeFile(self):
        vf = open(self.FileName+'.out', 'w')
        try:
            vN = 0
            for v in self.ResCases:
                vN += 1
                vf.write("Case #%d: %d\n" % (vN, v))
            vf.close()
        except:
            vf.close()
            raise

def main():
    v = Prob()
    v.init('/home/nuno/google/A-large.in')
    v.readFile()
    v.procCases()
    v.writeFile()
    pass

if __name__ == '__main__':
    main()
