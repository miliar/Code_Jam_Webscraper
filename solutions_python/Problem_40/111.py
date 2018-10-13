import sys

def main():
    line = sys.stdin.readline().strip()

    testCaseCnt = int(line);

    for testCaseNum in range(testCaseCnt):
        line = sys.stdin.readline().strip()

        treeAsString = ''
        for i in range(int(line)):
            line = sys.stdin.readline()
            treeAsString += line
        treeAsString = treeAsString.replace('(', ' ( ')
        treeAsString = treeAsString.replace(')', ' ) ')
        treeTokens = treeAsString.split()
        tree = {}
        allAttributes = set()
        readTree(treeTokens, 0, '', 1.0, tree, allAttributes)        

        print 'Case #%d:' % (testCaseNum + 1)
        line = sys.stdin.readline().strip()
        animalCnt = int(line)
        for animalNum in range(animalCnt):
            line = sys.stdin.readline().strip()
            values = line.split()
            animalAttributes = set([''])
            for attribute in values[2:]:
                animalAttributes.add(attribute)
            for attribute in allAttributes:
                if not attribute in animalAttributes:
                    animalAttributes.add('!' + attribute)
            p = findP(tree, animalAttributes)
            print '%0.7f' % p
       

def readTree(tokens, tokenNum, path, lastP, tree, allAttributes):
    tokenNum += 1
    p = float(tokens[tokenNum])
    tokenNum += 1
    if tokens[tokenNum] <> ')':
        attribute = tokens[tokenNum]        
        tokenNum += 1
        allAttributes.add(attribute)
        tokenNum = readTree(tokens, tokenNum, path + '/' + attribute, p * lastP, tree, allAttributes)
        tokenNum = readTree(tokens, tokenNum, path + '/!' + attribute, p * lastP, tree, allAttributes)
    else:
        tree[path] = p * lastP
    tokenNum += 1
    return tokenNum

def findP(tree, animalAttributes):
    for path in tree:
        treeAttributes = path.split('/')       
        match = True
        for treeAttribute in treeAttributes:
            if not treeAttribute in animalAttributes:
                match = False
        if match:
            return tree[path]
    return 0.0

if __name__ == "__main__":
    main()
