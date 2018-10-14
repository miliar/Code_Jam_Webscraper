#!/usr/bin/python2.6 -tt
def openFile(path, right):
    file = open(path, right)
    return file
    
def closeFile(file):
    file.close()
    
def getLine(lineNum, file):
    for i in range(4):
        if( lineNum == (i+1) ):
            res = str(next(file))
        else:
            waste = str(next(file))
    return res
    
def solve(l1, l2):
    l1 = map(int, l1.split())
    l2 = map(int, l2.split())
    cpt = 0
    res = 0
    for i in range(4):
        for j in range(4):
            if(l1[i] == l2[j]):
                cpt = cpt + 1
                res = l1[i]
    if(cpt == 1):
        return str(res)
    if(cpt > 1):
        return "Bad magician!"
    if(cpt == 0):
        return "Volunteer cheated!"
        
def main():
    path = "source.in"
    output = "output"
    file = openFile(path, "rU")
    outputFile = openFile(output, "wb")
    
    for i in range(int(next(file))):
        outputFile.write(str("Case #" + str( i + 1 ) + ": "))
        line1 = getLine(int(next(file)), file)
        line2 = getLine(int(next(file)), file)
        outputFile.write(solve(line1, line2))
        outputFile.write("\n");
    
    closeFile(file)
    closeFile(outputFile)
	
#launch the main function
if __name__ == '__main__':
	main()