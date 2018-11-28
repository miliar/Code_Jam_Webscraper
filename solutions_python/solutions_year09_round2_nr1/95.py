#!/usr/bin/python

import sys

def getNumber(s):
    #print s
    # We read until we encounter a letter or a closing parenthesis
    i = 0
    while (not s[i].isalpha()) and (not s[i] == ")") :
        i = i + 1
    return s[:i]

def getFeature(s):
    s = s.strip()
    i = 0
    while s[i].isalpha():
        i = i + 1
    return s[:i]

def readTree(s):
    # Recursive descent parser
    # We throw away whitespace
    #print "Me piden",s
    s = s.strip()
    s = s[1:] # We throw away (
    weight = getNumber(s).strip()
    #print "Peso",weight
    s = s.strip()[len(weight):].strip()
    weight = eval(weight)
    if s[0] == ")":
        return ((weight,),s[1:])
    else:
        feature = getFeature(s).strip()
        s = s[len(feature):].strip()
        (leftTree,rest) = readTree(s)
        #print "resto",rest
        (rightTree,rest) = readTree(rest.strip())
        return ((weight,feature,leftTree,rightTree),rest.strip()[1:])

def line():
    return sys.stdin.readline()[:-1]

def readList():
    return map(eval,line().split())

# print readTree("(0.5 lindo (0.1) (0.2) )")
# print getNumber("1.000)")

def computeProbability(name,features,tree,p):
    if len(tree) == 1: # We have a leaf
        return p * tree[0]
    else:
        (weight,feature,left,right) = tree
        if feature in features:
            return computeProbability(name,features,left,p*weight)
        else:
            return computeProbability(name,features,right,p*weight)

if __name__ == '__main__':
    numberOfCases = eval(line())
    for caseNumber in range(numberOfCases):
        L = eval(line())
        tree = []
        for i in range(L):
            tree.append(line().strip())
        tree = ' '.join(tree)
        tree = readTree(tree)[0]
        A = eval(line())
        print "Case #" + str(caseNumber+1) + ":" 
        for i in range(A):
            animalSpec = line().split()
            name,features = animalSpec[0],set(animalSpec[2:])
            print "%.7f" % computeProbability(name,features,tree,1)
