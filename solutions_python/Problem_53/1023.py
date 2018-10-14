'''
Created on May 8, 2010

@author: Abo Yassin
'''

import sys
import os

class snapper:
        
    prev_snapper = None
    state = "OFF"
    
    def __init__(self, prev_snapper):
        self.prev_snapper = prev_snapper
    
    def snap(self):
        if self.prev_snapper == None or self.prev_snapper.output_power():
            if self.state == "OFF":
                self.state = "ON"
            elif (self.state == "ON"):
                self.state = "OFF"
        
                
    def output_power(self):
        if (self.prev_snapper == None or self.prev_snapper.output_power() ) and self.state == "ON":
            return True
        else:
            return False

def parseInputFile(filePath):
    inputFile = open(filePath, 'r')
    fileName, extension = os.path.splitext(filePath)
    outputFile = open(fileName + '.out', 'w')
    T = int(inputFile.readline().strip())    
    for i in range(T):
        tokens = inputFile.readline().strip().split(" ")
        N = int(tokens[0])
        K = int(tokens[1])        
        
        snappers = []                        
        for j in range(N):
            try:
                s = snapper(snappers[len(snappers) - 1])
            except IndexError, e:
                s = snapper(None)
            snappers.append(s)
        snappers.reverse()
        for k in range(K):
            for l in range(len(snappers)):
                snappers[l].snap()
        status = ""
        if snappers[0].output_power():
            status = "ON"
        else:
            status = "OFF"
        outputFile.write("Case #" + str(i + 1) + ": " +  status + "\n")        
    outputFile.close() 
    inputFile.close()       
        
if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print 'you need to specify input file path.'
        sys.exit(1)
    
    parseInputFile(sys.argv[1])