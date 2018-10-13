import sys
from math import *
import operator

def main():
    # read in command-line arguments
    junk, testFile = sys.argv
    
    data = open(testFile,'r').read().splitlines()
    
    T = int(data[0])
    caseNum = 1
    line = 1
    while line < len(data):
        # read instance, advance line
        n = data[line] # vector length
        line += 1
        
        v1 = map(int,data[line].split())
        line += 1
        
        v2 = map(int,data[line].split())
        line += 1
    
        # get down to business
        z = zip(sorted(v1), sorted(v2, reverse=True))
        tot = sum([x*y for (x,y) in z])
        
        print('Case #' + str(caseNum) + ': ' + str(tot))
        caseNum += 1
    
if __name__ == "__main__":
    main()
