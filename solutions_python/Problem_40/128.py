import math
import sys
#import random

class node:
    #def __init__(self):
    
    def setProb(self, prob):
        self.prob = prob
        self.nextYes = 0
        self.nextNo = 0
        self.word = 0
        
    def setWord(self, word):
        self.word = word
    
    def setYes(self, nextYes):
        self.nextYes = nextYes

    def setNo(self, nextNo):
        self.nextNo = nextNo
        
    def getProb(self):
        return self.prob

    def getYes(self):
        return self.nextYes
    
    def getNo(self):
        return self.nextNo

    def getWord(self):
        return self.word
    
        
def doCase():
    global numLinesLeft
    result = ""
    numLinesLeft = int(sf.readline())
    tree = buildTree()
    while (numLinesLeft>0):
        sf.readline()
        numLinesLeft -= 1
    numAnimals = int(sf.readline())
    for i in range(0,numAnimals):
        animal = sf.readline().strip('\n').split(' ')
        animal = set(animal[2:])
        result += "%10.7f" % (getCuteProb(animal, tree))
        if (i<numAnimals-1):
            result += "\n"
    return result


def buildTree():
    global numLinesLeft
    tree = node()
    line = list()
    while len(line)==0:
        numLinesLeft = numLinesLeft - 1
        lineT = sf.readline().replace('(','').replace(')','').strip('\n').split(' ')
        for i in range(0,len(lineT)):
            if (lineT[i]!='' and lineT[i]!='(' and lineT[i]!=')'):
                line.append(lineT[i])
    if (len(line)==1):
        tree.setProb(float(line[0]))
    if (len(line)==2):
        tree.setProb(float(line[0]))
        tree.setWord(line[1])
        tree.setYes(buildTree())
        tree.setNo(buildTree())
    return tree

def getCuteProb(animal, tree):
    p = tree.getProb()
    if (tree.getWord() in animal):
        if (tree.getYes()==0):
            return p
        else:
            return p*getCuteProb(animal, tree.getYes())
    else:
        if (tree.getNo()==0):
            return p
        else:
            return p*getCuteProb(animal, tree.getNo())



def processFile(source, target):
    global sf #want to read file in all functions
    sf = open(source)
    tf = open(target,"w")
    T = sf.readline()
    T = int(T)
    for case in range(1, T+1):
        result = doCase()
        newline = 'Case #' + str(case) + ':\n' + str(result)
        print newline
        tf.write(newline)
        if not case==T: tf.write('\n')
    sf.close
    tf.close
        
def main(argv = None):
    if argv is None:
        argv = sys.argv
    if (len(argv)>2):
        processFile(argv[1], argv[2])
    
if __name__ == "__main__":
    main()
    