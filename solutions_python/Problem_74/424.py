'''
Created on Apr 30, 2011

@author: Marius Dorin Moraru
'''

#filename without extension
#fileName = raw_input("Enter a name:")
fileName = "c:/learn/a"

inFile = open(fileName + ".in", "rU")
outFile = open(fileName + ".out", "w")

nrOfTestCases = long(inFile.readline());        
print "nrOfTestCases " + str(nrOfTestCases)








def readTestCase():   
    v = inFile.readline().replace("\n","").replace("\r","").split(" ")[1:]    
    return v






#resolve testCase
def resolve(data):   
    oLastPos=1;
    oLastActionTime = 0;
    bLastPos=1;
    bLastActionTime=0;
    cTime=0;    
    
    for i in xrange(len(data) / 2):
        if data[2*i] == "B":
            pos = int(data[2*i+1])
            cTime = cTime + max((abs(pos - bLastPos)) - (cTime-bLastActionTime),0) + 1;
            bLastPos = pos;
            bLastActionTime = cTime;
        elif data[2*i] == "O":
            pos = int(data[2*i+1])
            cTime = cTime + max((abs(pos - oLastPos)) - (cTime-oLastActionTime),0) + 1;
            oLastPos = pos;
            oLastActionTime = cTime;
        
    #print cTime;
    return cTime








for i in range(nrOfTestCases):
    print "resolving testCase " + str(i + 1)
    out = resolve(readTestCase())
    outFile.writelines("Case #" + str(i + 1)+": " + str(out) + "\n")
outFile.close()


    
        