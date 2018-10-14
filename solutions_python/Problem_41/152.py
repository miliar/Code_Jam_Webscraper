inFile = open("../B-small.in", "r")
outFile = open("../B-sol.txt", "w")


class TreeNode:
    def __init__(self, parent, value, digitStr):
        self.parent = parent
        self.children = []
        availDigits = [digitStr[i] for i in range(len(digitStr))]
        self.value = value
        if len(availDigits) == 1:
            self.value = self.value + availDigits[0]
            return
        
        availDigits.sort()
        lastDigit = None
        for digit in availDigits:
            if digit == lastDigit:
                continue
            newDigList = availDigits[:]
            newDigList.remove(digit)
            
            self.children.append(TreeNode(self, value + digit, "".join(newDigList)))
            lastDigit = digit
    

numTests = int(inFile.readline().strip())

for testNum in range(numTests):
    curNum = inFile.readline().strip()
    root = TreeNode(None, "", curNum)
    q = []
    q.append(root)
    nextNum = ""
    while not len(q) == 0:
        curNode = q.pop(0)
        if curNode.value == curNum:
            if not len(q) == 0:
                nextNode = q.pop(0)
                nextNum = nextNode.value
            break
        for child in curNode.children:
            q.append(child)
    
    if nextNum == "":
        availDigits = [curNum[i] for i in range(len(curNum))]
        availDigits.sort()
        zeroCount = 0
        for digit in availDigits:
            if digit == "0":
                zeroCount += 1
        
        for j in range(zeroCount):
            availDigits.remove("0")
            
        for j in range(len(availDigits)):
            nextNum = nextNum + availDigits[j]
            if j == 0:
                nextNum = nextNum + "0"
                for k in range(zeroCount):
                    nextNum += "0"
        
    
    outFile.write("Case #" + str(testNum+1) + ": " + nextNum + "\n")