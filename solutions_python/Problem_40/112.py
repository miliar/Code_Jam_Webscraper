inFile = open("../A-large.in", "r")
outFile = open("../A-sol.txt", "w")

numTests = int(inFile.readline().strip())


class CuteTreeNode:
    def __init__(self):
        myTokens = inFile.readline().replace("(", "").replace(")", "").strip().split(" ")
        while myTokens[0] == '' and len(myTokens) == 1:
            myTokens = inFile.readline().replace("(", "").replace(")", "").strip().split(" ")

        if myTokens[0] == "":
            pass
        self.weight = float(myTokens[0])

        self.name = None
        self.yes = None
        self.no = None
        if (len(myTokens) > 1):
            self.name = myTokens[1]
            self.yes = CuteTreeNode()
            self.no = CuteTreeNode()
    
    def cutify(self, attrList):
        if self.name == None:
            return self.weight
        if self.name in attrList:
            return self.weight * self.yes.cutify(attrList)
        else:
            return self.weight * self.no.cutify(attrList)

for testNum in range(numTests):
    treeLines = int(inFile.readline().strip())
    rootNode = CuteTreeNode()
    
    nextLine = inFile.readline().replace("(", "").replace(")", "").strip()
    while nextLine == "":
        nextLine = inFile.readline().replace("(", "").replace(")", "").strip()
    
    numAnimals = int(nextLine)
    outFile.write("Case #" + str(testNum+1) + ":\n")
    for animNum in range(numAnimals):
        line = inFile.readline().strip().split(" ")
        attrList = []
        for i in range(int(line[1])):
            attrList.append(line[2 + i])
        outFile.write(("%.7f" % rootNode.cutify(attrList)) + "\n")