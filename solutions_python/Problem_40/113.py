class TreeNode:
    coef = None
    desc = None
    child1 = None
    child2 = None

counter = 0
treeList = []
    
def readTreeNode():
    global counter
    global treeList
    
    counter += 1
    node = TreeNode()
    node.coef = float(treeList[counter])
    counter += 1
    
    if treeList[counter] != '(' and treeList[counter] != ')':
        node.desc = treeList[counter]
        counter += 1
        
    if treeList[counter] == '(':
        node.child1 = readTreeNode()
        
    if treeList[counter] == '(':
        node.child2 = readTreeNode()
    
    if treeList[counter] == ')':
        counter += 1
        
    return node
         
def traverseTree(treeNode, animal):
    if treeNode.desc == None:
        return treeNode.coef
    elif treeNode.desc in animal[1:]:
        return treeNode.coef * traverseTree(treeNode.child1, animal)
    else:
        return treeNode.coef * traverseTree(treeNode.child2, animal)
    
INPUT_FILE = 'inputs/A-large.in'
OUTPUT_FILE = 'outputs/A-large.out'

f_in = open(INPUT_FILE, 'r')
f_out = open(OUTPUT_FILE, 'w+')

N = int(f_in.readline().strip())

for i in range(N):
    L = int(f_in.readline().strip())
    treeStr = ''
    for j in range(L):
        treeStr += f_in.readline()
        
    A = int(f_in.readline().strip())
    animals = []
    for a in range(A):
        animals.append(f_in.readline().strip().split())
        del animals[a][1]
        
    treeStr = treeStr.replace('\n', ' ').replace('(', ' ( ').replace(')', ' ) ')
    
    treeList = treeStr.split();
    counter = 0
    rootNode = readTreeNode()
    
    probs = [1.0] * len(animals)
    for a, animal in enumerate(animals):
        probs[a] = traverseTree(rootNode, animal)
    
    print("Case #" + str(i + 1) + ":\n")
    f_out.write("Case #" + str(i + 1) + ":\n")
    for p in probs:
        print('%.7F\n' % p)
        f_out.write('%.7F\n' % p) 
#    f_out.write("Case #" + str(i + 1) + ": " + str(p) + "\n")

f_in.close()
f_out.close()
