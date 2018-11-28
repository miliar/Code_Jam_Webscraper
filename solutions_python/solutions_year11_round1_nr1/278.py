'''
Created on Apr 30, 2011

@author: Marius Dorin Moraru
'''
import math

#filename without extension
#fileName = raw_input("Enter a name:")
fileName = "c:/learn/a"

inFile = open(fileName + ".in", "rU")
outFile = open(fileName + ".out", "w")

nrOfTestCases = long(inFile.readline());        
print "nrOfTestCases " + str(nrOfTestCases)


def readTestCase():   
    v = inFile.readline().split(" ")
    n = long(v[0])
    pd = float(v[1])
    pg = float(v[2])
    return [n, pd, pg] 


#resolve testCase
def resolve(data):
    n = data[0]
    pd = data[1] / 100
    pg = data[2] / 100
    print n, pd, pg
    
    if n < 100:
        while n > 0:
            if (n * pd) == round(n * pd):
                _pd = float(1 - pd);
                if str(float(n * _pd)) == str(round(n * _pd)):
                    print n
                    break;
            n = n - 1;
        if n == 0:
            return "Broken"
    if pd > 0 and pg == 0:
        return "Broken"
    if pd == 0 and pg > 0:
        return "Broken"
    if pd < 1 and pg == 1:
        return "Broken"
    return "Possible"







for i in range(nrOfTestCases):
    print "resolving testCase " + str(i + 1)
    out = resolve(readTestCase())
    outFile.writelines("Case #" + str(i + 1)+": " + str(out) + "\n")
outFile.close()


    
        