'''
Created on Apr 13, 2012

@author: aaron
'''

class CoreCodeJam(object):
    '''
    A class designed to make use of the standard input and output formats used in code jam
    '''
    
    def runAllCases(self):
        for case in self.cases:
            yield self.runCase(case)
    
    def getNumCases(self):
        return len(self.cases)
    
    def writeResults(self, outfile):
        for i, result in enumerate(self.runAllCases()):
            self.writeResult(i+1, result, outfile)
    
    def writeResult(self, caseNum, result, outfile):
        outfile.write("Case #{0}: {1}\n".format(caseNum, result))

    def __init__(self, infile):
        lines=infile.readlines()
        if int(lines[0])!=len(lines)-1:
            raise Exception("Invalid number of test cases")
        self.cases=lines[1:]
        