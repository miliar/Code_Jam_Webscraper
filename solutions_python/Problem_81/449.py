def sumc(iLst, iexcl=-1):
#            print iLst
            t = 0
            n = 0
            for v in range(len(iLst)):
                if v != iexcl:
                    if iLst[v] != '.':
                        t += int(iLst[v])
                        n += 1
            if n > 0:
                r = (t+0.0)/n
            else:
                r = 0
            return (t, n, r)

def calcOWP(iLstS):
        vRes = []
        for e in range(len(iLstS)):
            t = 0
            n = 0
            for v in range(len(iLstS[e])):
                if v != e and iLstS[e][v] != '.':
                    t += sumc(iLstS[v], e)[2]
                    n += 1
            vOWP = (t+0.0) / n
            vRes.append(vOWP)
        return (vRes)

class Prob:
    def __init__(self):
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
                vN = int(vf.readline())
                vLstS = []
                for vN in range(int(vN)):
                    vLstS.append(vf.readline()[:-1])
                self.LstCases.append(vLstS)
            vf.close()
        except:
            vf.close()
            raise

    def procCase(self, iLstS):
        #print iLstS
        vRes = []
        vLstOWP = calcOWP(iLstS)
        for e in range(len(iLstS)):
            #WP
            t = 0
            n = 0
            vWP = sumc(iLstS[e])[2]
            #OWP
            vOWP = vLstOWP[e]
            #print e, vOWP
            #OOWP
            t = 0
            n = 0
            for v in range(len(iLstS[e])):
                if v != e and iLstS[e][v] != '.':
                    t += vLstOWP[v]
                    n += 1
            vOOWP = (t+0.0) / n
            # RPI
            vRPI = 0.25 * vWP + 0.50 * vOWP + 0.25 * vOOWP
            vRes.append(vRPI)
        return (vRes)
        pass
    
    def procCases(self):
        vN=0
        for v in self.LstCases:
            #print v
            vN += 1
            print "Case #%d" % vN
            self.ResCases.append(self.procCase(v))

    def writeFile(self):
        #print self.ResCases
        vf = open(self.FileName+'.out', 'w')
        try:
            vN = 0
            for v in self.ResCases:
                vN += 1
                vf.write("Case #%d:\n" % (vN))
                for r in v:
                    vf.write("%f\n" % r)
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
