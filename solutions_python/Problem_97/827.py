'''
Created on Apr 13, 2012

@author: conan
'''

from __future__ import print_function
import sys, os, re, numpy

#===============================================================================
# a = numpy.array([
# [1, 2],
# [1, 2]
#               ])
# 
# b = numpy.array([
# [1, 2],
# [1, 2]
#               ])
# 
# x = numpy.linalg.solve(a, b)
#===============================================================================



#change current working directory
CWD = 'C:/Users/conan/eclipseProjects/myPyLib/src/root/codejam/'
DESKTOP = 'C:/Users/conan/Desktop/'
os.chdir(CWD)

def cutPaste():
    for f in os.listdir(DESKTOP):
        if f.endswith('.in'):
            os.rename(DESKTOP + f, CWD + f)
            print('"%s" ---> "%s"' % (DESKTOP + f, CWD + f))
    

def submit(caseFunc, inFile, outFile='output.out'):
    ipt = Input(inFile)
    #print to file or to stdout
    outFile = outFile and open(CWD + outFile, 'w') or sys.stdout
    for caseNum in range(ipt.nCase):
        print ('Case #%d: %s' % (caseNum + 1, caseFunc(ipt)), file=outFile)
    print('submission finished')

class Input(object):
    def __init__(self, string):
        if string.endswith('.in'):
            string = open(CWD + string).read()
        self.string = string
        self.iterator = iter(string.split('\n'))
        self.nCase = int(self.nextLine())
    
    def nextLine(self, sep=None, toInt=False):
        rv = ''
        while (rv == ''):
            rv = self.iterator.next()
        if sep is not None: rv = rv.split(sep)
        if toInt: 
            rv = map(int, rv)
        return rv
  
if __name__ == '__main__':
    pass
