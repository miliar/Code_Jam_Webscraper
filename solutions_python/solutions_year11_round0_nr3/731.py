        
class Prob:
    def __init__(self):
        self.LstCases = []  # each list of ints
        self.ResCases = []  # output each item is case output
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
                vLn = vf.readline() # No. of candies
                vLn = vf.readline()
                vLst = [int(v) for v in vLn.split()]
                self.LstCases.append(vLst)
            vf.close()
        except:
            vf.close()
            raise

    def procCase(self, iLst):
        # Patricks sum is like Xor
        iLst.sort()
        iLst.reverse()
        vLstSelCand = [0]*len(iLst)
        vMaxVal = -1    # result Max of vSumBS
        vSumBS = 0      # Sum of Bag with selected candies (vLstSelCand[n] == 0)
        vXBS = 0        # Xor of selected candies
        vXBO = 0        # Xor of other bag
        for v in iLst:
            vSumBS += v
            vXBS ^= v

        vRestart = True
        while vRestart:
            vRestart = False
            vIdx = len(iLst)-1
            while vIdx >= 0:
                #print vLstSelCand
                if vLstSelCand[vIdx] == 0:
                    vLstSelCand[vIdx] += 1
                    vSumBS -= iLst[vIdx]
                    vXBS ^= iLst[vIdx]
                    vXBO ^= iLst[vIdx]
                    if vXBS == vXBO and vSumBS > vMaxVal:
                        vMaxVal = vSumBS
                    vRestart = False;
                    break
                else:
                    vLstSelCand[vIdx] -= 1
                    vSumBS += iLst[vIdx]
                    vXBS ^= iLst[vIdx]
                    vXBO ^= iLst[vIdx]
                    vIdx -= 1

        if vMaxVal == -1:
            vRes = 'NO'
        else:
            vRes = str(vMaxVal)
        print vRes
        return vRes
    
    def procCases(self):
        vN=0
        for v in self.LstCases:
            vN += 1
            print "Case #%d" % vN,
            self.ResCases.append(self.procCase(v))

    def writeFile(self):
        vf = open(self.FileName+'.out', 'w')
        try:
            vN = 0
            for v in self.ResCases:
                vN += 1
                vf.write("Case #%d: %s\n" % (vN, v))
            vf.close()
        except:
            vf.close()
            raise

def main():
    v = Prob()
    v.init('/home/nuno/google/C-large.in')
    v.readFile()
    v.procCases()
    v.writeFile()
    pass

if __name__ == '__main__':
    main()
