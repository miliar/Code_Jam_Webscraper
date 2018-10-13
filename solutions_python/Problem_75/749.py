        
class Prob:
    def __init__(self):
        self.LstCases = []  # each item (case) is 3 lists: "LstC", "LstD", StrI
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
                vLn = vf.readline()
                vLst = vLn.split()
                vNC = int(vLst[0])
                vND = int(vLst[vNC+1])
                vLstC = vLst[1: vNC+1]
                vLstD = vLst[vNC+2: vNC+vND+2]
                vIn = vLst[vNC+vND+3]
                self.LstCases.append([vLstC, vLstD, vIn])
            vf.close()
        except:
            vf.close()
            raise

    def procCase(self, iLst):
        # init Robot
        vDicC = {}
        vLstD = []
        vStrI = [] 
        vLstO = []
        # Combinations
        for v in iLst[0]:
            vDicC[v[2]] = [v[0:2], v[1]+v[0]]
        # Oppositions
        for v in iLst[1]:
            vLstD.append(v[0:2])
            vLstD.append(v[1]+v[0])

#        print
#        print vDicC
#        print vLstD
#        print iLst[2]
        
        # Translate string
        vLstO = []
        for vNxt in iLst[2]:
            if len(vLstO) > 0:
                # Test combinations
                vP = vLstO[-1]+vNxt
                vCFnd = False;
                for v in vDicC:
                    if vP in vDicC[v]:
                         vLstO.pop()
                         vLstO.append(v)
                         vCFnd = True
                         break
                if not vCFnd:
                    # test oppositions
                    vDFnd = False;
                    for vPrev in vLstO:
                        vP = vPrev+vNxt
                        if vP in vLstD:
                            vLstO = []
                            vDFnd = True
                            break
                    if not vDFnd:
                        vLstO.append(vNxt)
            else:
                vLstO.append(vNxt)
        print vLstO
        return (vLstO)
    
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
                vf.write("Case #%d: [%s]\n" % (vN, ', '.join(v)))
            vf.close()
        except:
            vf.close()
            raise

def main():
    v = Prob()
    v.init('/home/nuno/google/B-small-attempt0.in')
    v.readFile()
    v.procCases()
    v.writeFile()
    pass

if __name__ == '__main__':
    main()
