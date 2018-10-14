'''
Created on 14.04.2012

@author: GreatCombinator
'''

import math
import os.path

class Googlers(object):
    def __init__(self, iPath, oPath):
        self.iPath = iPath
        self.oPath = oPath
        self.nrOfTestCases = 0
        self.testCases = []
        
    def solve(self):
        fin = open(self.iPath, 'r')
        lines = fin.readlines()
        self.nrOfTestCases = int(lines[0])
        idx = 1
        fout = open(self.oPath, 'w')
        while idx < len(lines)-1:
            tc = lines[idx].split()
            tc = [int(nr) for nr in tc]
            fout.write('Case #%s: %s\n' % (idx, self.computeTestCase(tc[0], tc[1], tc[2], tc[3:])))
            print 'Case #%s: %s' % (idx, self.computeTestCase(tc[0], tc[1], tc[2], tc[3:]))
            idx += 1
        tc = lines[idx].split()
        tc = [int(nr) for nr in tc]
        fout.write('Case #%s: %s' % (idx, self.computeTestCase(tc[0], tc[1], tc[2], tc[3:])))
        print 'Case #%s: %s' % (idx, self.computeTestCase(tc[0], tc[1], tc[2], tc[3:]))
        fout.close()
        fin.close()
    
    def computeTestCase(self, nrGooglers, nrSurp, p, tis):
        tis.sort()
        counter = 0
        surpCounter = 0
        idx = 0
        while idx<len(tis):
            ceil = math.ceil(float(tis[idx]/3.0))
            if ceil == 10 or ceil == 0 and ceil >= p:
                counter += 1
            elif ceil < 10 and ceil > 0 and surpCounter<nrSurp and (ceil + 1) >= p:
                counter += 1
                surpCounter += 1
            elif ceil<10 and ceil > 0 and ceil >= p:
                counter += 1
            idx+=1
        return counter

if __name__ == '__main__':
    iPath = os.path.join('.', 'B-small-attempt0.in')
    oPath = os.path.join('.', 'B-small-attempt0.out')
    googlers = Googlers(iPath, oPath)
    '''print googlers.computeTestCase(3, 1, 5, [15,13,11])
    print googlers.computeTestCase(3, 0, 8, [23,22,21])
    print googlers.computeTestCase(2, 1, 1, [8,0])
    print googlers.computeTestCase(6, 2, 8, [29,20,8,18,18,21])'''
    googlers.solve()