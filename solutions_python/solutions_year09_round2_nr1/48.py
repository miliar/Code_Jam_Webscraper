import fileinput
import string

NEWLINE_TO_SPACE = string.maketrans("\n\r","  ")

#current_line = bonus_string[0] + fi.next()
#current_line.translate(NEWLINE_TO_SPACE).split()

class DecisionNode(object):
    def __init__(self,tokenizedString):
        splitTokens = tokenizedString[0]
        #print "parsing:",splitTokens
        assert(splitTokens[0][0] == '(')
        if splitTokens[0] == '(':
            del splitTokens[0]
            #print splitTokens[0][-1]
        else:
            splitTokens[0] = splitTokens[0][1:]
            #print "Removed brace"
        if splitTokens[0][-1] == ')' or splitTokens[1][0] == ')':
            if splitTokens[0][-1] == ')':
                #print "Hi there"
                #print splitTokens[0][:-1]
                self.prob = float(splitTokens[0][:-1])
            else:
                self.prob = float(splitTokens[0])
                splitTokens[1] = splitTokens[1][1:]
                if len(splitTokens[1]) == 0:
                    del splitTokens[1]
            tokenizedString[0] = splitTokens[1:]
            self.feature = None
            return
        self.prob = float(splitTokens[0])
        self.feature = splitTokens[1]
        tokenizedString[0] = splitTokens[2:]
        self.childTrue = DecisionNode(tokenizedString)
        self.childFalse = DecisionNode(tokenizedString)
        assert(tokenizedString[0][0] == ')')
        del tokenizedString[0][0]
        
    def getProb(self,featuresList):
        childProb = 1.0
        if self.feature != None:
            if self.feature in featuresList:
                childProb = self.childTrue.getProb(featuresList)
            else:
                childProb = self.childFalse.getProb(featuresList)
        return self.prob*childProb

def parseTree(numLines,fi):
    txt = []
    #print "Reading",numLines
    txt = [fi.next() for x in range(numLines)]
    s = "".join(txt)
    #print s
    s = s.translate(NEWLINE_TO_SPACE)
    #print s
    tokens = s.split()
    return DecisionNode([tokens])

def checkAnimals(numLines,tree,fi):
    for i in range(numLines):
        l = fi.next()
        splt = l.split()
        assert int(splt[1]) == len(splt) - 2
        features = splt[2:]
        print "%0.8f" % tree.getProb(features)

def main():
    fi = fileinput.input()
    caseCount = int(fi.next())
    for i in range(caseCount):
        treeLen = int(fi.next())
        tree = parseTree(treeLen,fi)
        animalsLen = int(fi.next())
        print "Case #%d:" % (i+1)
        checkAnimals(animalsLen,tree,fi)

if __name__ == "__main__":
    main()
        
        
        
            
            
        
        
