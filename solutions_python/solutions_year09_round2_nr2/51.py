import re,sys

class TestGroup:
    base = ord('0')
    
    def __init__(self):
        pass

    def readListLine(self):
        return self.input.readline().strip().split()

    def processFile(self,filename):
        self.input=open(filename,"r")
        if filename.endswith(".in"):
            filename=filename[:-3]
        filename+=".out"
        self.output=open(filename,"w")

        self.testCaseCount=int(self.readListLine()[0])
        for self.testCaseNum in range(1,self.testCaseCount+1):
            # todo read args
            arg=self.readListLine()[0]
            self.initCase()
            self.prepCase()
            self.runCase(arg)
            pass
        
        self.debug("-----------done------------")
        self.output.close()
        self.input.close()

    def debug(self,text):
        print text

    def initCase(self):
        self.debug("-----initCase #%d of %d------"%(self.testCaseNum,self.testCaseCount))
        return

    def prepCase(self):
        self.debug("prepCase #%d"%self.testCaseNum)
        return

    def runCase(self,N):
        self.debug("runCase #%d"%self.testCaseNum)
        r="0"+N
        self.debug("N= %s"%r)
        
        left=r[:-1]
        right=r[-1]
        
        while left and left[-1]>=right[0]:
            right=left[-1]+right
            left=left[:-1]
        print left,right

        right=list(right)
        right.sort()

        for i in range(len(right)):
            if right[i] >left[-1]:
                right.append(left[-1])
                left=left[:-1]+right[i]
                del right[i]
                break
        right.sort()

        print left,right

        right=list(right)
        right.sort()
        
        r=left+("".join(right))
        while r[0]=="0":
            r=r[1:]
        self.debug("Case #%d: %s=>%s"%(self.testCaseNum,N,r))
        self.output.write("Case #%d: %s\n"%(self.testCaseNum,r))
        return
        

e=TestGroup()
e.processFile(sys.argv[1])