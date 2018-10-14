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
    v = inFile.readline().replace("\n","").replace("\r","").split(" ")
    n = long(v[0])
    l = long(v[1])
    h = long(v[2])
    v = inFile.readline().replace("\n","").replace("\r","").split(" ")
    for i in xrange(n):
        v[i] = long(v[i])
    return n, l, h, v

#resolve testCase
def resolve(data):
#    print data
    n = data[0]
    l = data[1]
    h = data[2]
    v = data[3]
    
    for i in xrange(l, h + 1):
        b = 1;
        for j in xrange(n):
            if v[j]%i != 0 and i%v[j] != 0:
                b = 0;
                break
        if b == 1:
            return i
            
    return "NO";







for i in range(nrOfTestCases):
    print "resolving testCase " + str(i + 1)
    out = resolve(readTestCase())
    outFile.writelines("Case #" + str(i + 1)+": " + str(out) + "\n")
outFile.close()


    
        