# input formatting
class FileWrapper:
    def __init__(self, file):
        self.file = file
    
    def getInt(self):
        return int(self.file.readline())
    
    def getInts(self):
        return [int(z) for z in self.file.readline().split()]
    
    def getFloat(self):
        return float(self.file.readline())
    
    def getFloats(self):
        return [float(z) for z in self.file.readline().split()]
    
    def getWords(self):
        return self.file.readline().split()
    
    def readline(self):
        return self.file.readline().strip()
    
    def close(self):
        self.file.close


# formatted printing
caseNum = 1
def printCase(result, resetNum=None):
    global caseNum
    if resetNum: caseNum = resetNum 
    print "Case #{0}: {1}".format(caseNum, result)
    caseNum += 1
    
