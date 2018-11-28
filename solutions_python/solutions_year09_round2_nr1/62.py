import re,sys

class Node:
    def __init__(self,weight):
        self.weight=float(weight)
        self.feature=None
        self.yesNode=None
        self.noNode=None
        pass
        
    def test(self,v,features):
        v*=self.weight
        if self.feature and self.feature in features:
            if self.yesNode:
                return self.yesNode.test(v,features)
        else:
            if self.noNode:
                return self.noNode.test(v,features)
        return v

class TestGroup:
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
            self.output.write("Case #%d:\n"%(self.testCaseNum))
            nLines=int(self.readListLine()[0])
            s=""
            for i in range(nLines):
                s+=" "+self.input.readline().strip()
            self.initCase(s)
            nAnimals=int(self.readListLine()[0])
            for i in range(nAnimals):
                args=self.readListLine()
                self.runCase(args[0],args[2:])
            pass
        
        self.debug("-----------done------------")
        self.output.close()
        self.input.close()

    def debug(self,text):
        print text

    def initCase(self,treeText):
        self.debug("-----initCase #%d of %d------"%(self.testCaseNum,self.testCaseCount))
        self.debug(repr(treeText))
        treeText=treeText.strip();
        weightPattern=re.compile(r"([\d.]+)(.*)")
        featurePattern=re.compile(r"([\w.]+)(.*)")
        stack=[]
        while treeText:
            if treeText[0]=="(":
                treeText=treeText[1:]
                pass
            elif treeText[0]==")":
                treeText=treeText[1:]
                node=stack.pop()
                if stack:
                    if not stack[-1].yesNode:
                        stack[-1].yesNode=node
                    else:
                        stack[-1].noNode=node
            else:
                match=weightPattern.match(treeText)
                if match:
                    weight=match.group(1)
                    treeText=match.group(2)
                    stack.append(Node(weight))
                else:
                    match=featurePattern.match(treeText)
                    if not match:
                        print "feature??? =>",treeText
                    stack[-1].feature=match.group(1)
                    treeText=match.group(2)
            treeText=treeText.strip()
        print stack
        self.root=node
        return

    def runCase(self,animal,features):
        self.debug("runCase #%d"%self.testCaseNum)
        self.debug(repr(animal))
        self.debug(repr(features))
        r=self.root.test(1.0,features)
        self.debug("%s = %.07f"%(animal,r))
        self.output.write("%.07f\n"%(r))
        return

e=TestGroup()
e.processFile(sys.argv[1])