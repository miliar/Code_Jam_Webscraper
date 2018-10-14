'''
Created on Apr 26, 2013
Google Code Jam Round A1 2013
Problem A

@author: Jared Feldman
'''

def getResult(radius, currentML):
    howManyRings = 1
    currentML = currentML - (pow(radius + 1, 2) - pow(radius, 2))

    radius += 2
    nextRingML = (pow(radius + 1, 2) - pow(radius, 2))
    
    while (nextRingML <= currentML):
        howManyRings += 1
        currentML -= nextRingML
        radius += 2
        nextRingML = (pow(radius + 1, 2) - pow(radius, 2))     
    
    
    return howManyRings

if __name__ == '__main__':
    # I/O Files
    readFile = open("A-small-attempt0.in","r+")
    writeFile = open("A-small-attempt0.out","w+")
    
    numberOfCases = int(readFile.readline())
    currentCase = 0
        
    # Loop through all cases
    while (currentCase < numberOfCases):
        # Increment case number
        currentCase += 1
        
        line = str.strip(readFile.readline())
        lineArray = str.split(line, " ")
        
        r = int(lineArray[0])
        t = int(lineArray[1])
        
        print "Case #%s: %s" %(currentCase, getResult(r, t))
        writeFile.write("Case #%s: %s\n" %(currentCase, getResult(r, t)))