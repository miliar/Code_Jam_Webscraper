inFile = open("../A-large.in", "r")
outFile = open("../A-sol.txt", "w")

numTests = int(inFile.readline().strip())

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.subNodes = {}
    
    def tryPath(self, dirs):
        if len(dirs) == 0:
            return 0
        
        if dirs[0] in self.subNodes:
            return self.subNodes[dirs[0]].tryPath(dirs[1:])
        else:
            self.subNodes[dirs[0]] = TreeNode(dirs[0])
            return 1 + self.subNodes[dirs[0]].tryPath(dirs[1:])
    
for testNum in range(numTests):
    existdirs, newdirs = map(int, inFile.readline().split())
    
    tree = TreeNode("/")
    for i in range(existdirs):
        dirs = inFile.readline().rstrip().split("/")
        tree.tryPath(dirs[1:])
    
    cost = 0
    for i in range(newdirs):
        dirs = inFile.readline().rstrip().split("/")
        cost += tree.tryPath(dirs[1:])
    
    outFile.write("Case #" + str(testNum+1) + ": " + str(cost) + "\n")
    print "Case #" + str(testNum+1) + ": " + str(cost)