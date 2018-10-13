'''
Created on Sep 12, 2009

@author: AliJ
'''

def parse_num():
    return map(int, raw_input().split())


def parse_tree(t, curPos):
    
    curPos=t.find("(", curPos)
    while t[curPos] in " (":
        curPos += 1
    firstBreak1 = t.find(" ", curPos)
    firstBreak2 = t.find(")", curPos)
    if firstBreak1 >= 0 and firstBreak1 < firstBreak2:
        firstBreak = firstBreak1
    else:
        firstBreak = firstBreak2
    prob = float(t[curPos:firstBreak])
    
    tree1Start = t.find("(", firstBreak)
    nextClose = t.find(")", firstBreak)
    if tree1Start < 0 or tree1Start > nextClose:
        return ([prob], nextClose+1)
    
    else:
        name = t[firstBreak:tree1Start].strip()
        (tree1, tree2Start) = parse_tree(t, tree1Start)
        (tree2, nextPos) = parse_tree(t, tree2Start)
        return ([prob, name, tree1, tree2], nextPos)



def getScore(treeL, features):
    
    if len(treeL) == 1:
        return treeL[0]
    elif treeL[1] in features:
        return treeL[0]*getScore(treeL[2], features)
    else:
        return treeL[0]*getScore(treeL[3], features) 


def process_case():
    
    L = int(raw_input())
    treeStr = ""
    for i in range(L):
        treeStr = treeStr + raw_input().strip() + " "
    treeL = parse_tree(treeStr, 0)[0]
    
    resultList = []
    A = int(raw_input())
    for i in range(A):
        animal = raw_input().split()
        n = int(animal[1])
        features = animal[2:2+n]
        
        resultList.append(getScore(treeL, features))
        
    
    return resultList


numCases = int(raw_input())

for i in range(numCases):
            
    print "Case #"+str(i+1)+":" 
    result = process_case()
    for j in result:
        print j