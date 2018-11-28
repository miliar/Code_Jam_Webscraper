k = 0
stalls = []
    
class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def setVal(self,value):
        self.rootid = value
    def getVal(self):
        return self.rootid

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left
            
def printTree(tree, level = 0):
        if tree != None:
            printTree(tree.getLeft(), level + 1)
            print ("\t" * level) + str(tree.getVal()) + "\n",
            printTree(tree.getRight(), level + 1)
    
def sit(root):
    node = root
##    printTree(root)
##    print "\n" * 3
    
    while node.getRight() != None:
        n = node.getVal()
        node.setVal(n - 1)
        
        if node.getRight().getVal() > node.getLeft().getVal():
            node = node.getRight()
        else:
            node = node.getLeft()
    
    n = node.getVal()
    
    if n % 2 == 0: #even
        node.setVal(n - 1)
        node.insertLeft(n/2 - 1)
        node.insertRight(n/2)
    else: #odd
        node.setVal(n - 1)
        node.insertLeft((n-1)/2)
        node.insertRight((n-1)/2)
    
    return node.getLeft().getVal(), node.getRight().getVal()
  
## I/O
t = int(raw_input())  # read a line with a single integer

for x in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case

    root = BinaryTree(n)
    LS, RS = 0, 0
    while k != 0:
        k = k - 1
        LS, RS = sit(root)
##        print str(LS) + "," + str(RS)
        

    y = max(LS,RS)
    z = min(LS,RS)
    
    print "Case #{}: {} {}".format(x, y, z)
    




