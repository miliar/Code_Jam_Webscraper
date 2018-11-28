'''
Created on 14.04.2012

@author: GreatCombinator
'''

import math
import os.path

class Recycled(object):
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
            fout.write('Case #%s: %s\n' % (idx, self.computeTestCase(tc[0], tc[1])))
            print 'Case #%s: %s' % (idx, self.computeTestCase(tc[0], tc[1]))
            idx += 1
        tc = lines[idx].split()
        tc = [int(nr) for nr in tc]
        fout.write('Case #%s: %s' % (idx, self.computeTestCase(tc[0], tc[1])))
        print 'Case #%s: %s' % (idx, self.computeTestCase(tc[0], tc[1]))
        fout.close()
        fin.close()
    
    def computeTestCase(self, A, B):
        counter = 0
        n = A
        while A < B:
            n = str(A)
            idx = -1
            while idx > -(len(str(A))):
                tmp = n[idx:] +  n[0:idx]
                tmp = int(tmp)
                if tmp <= B and tmp > A:
                    counter += 1
                idx -= 1
            A += 1
        return counter

if __name__ == '__main__':
    iPath = os.path.join('.', 'C-small-attempt0.in')
    oPath = os.path.join('.', 'C-small-attempt0.out')
    
    recycled = Recycled(iPath, oPath)
    recycled.solve()
    '''print googlers.computeTestCase(3, 0, 8, [23,22,21])
    print googlers.computeTestCase(2, 1, 1, [8,0])
    print googlers.computeTestCase(6, 2, 8, [29,20,8,18,18,21])'''