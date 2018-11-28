'''
Jirasak Chirathivat
'''
import psyco
psyco.full()

import os
import os.path
import sys
sys.setrecursionlimit(1000000000)
#### CHANGE HERE ####
filename = 'a.test'
#### CHANGE HERE ####

class Tree:
    def __init__(self):
        self.name = ''
        self.weight = 0
        self.top = None
        self.bottom = None

def findweight(line):
    #tmp = line.strip()
    tmp = line.replace('(','').replace(')','').strip()
    return float(tmp)

def createTree(treeline):
    #print treeline
    
    t = Tree()
    tmp = treeline[0].replace('(','').replace(')','').strip()
    if tmp.find(' ') < 0:
        t.name = None
        t.weight = float(tmp)
        return t
    
    i = treeline[0].find('(')
    j = i + 2
    
    split = treeline[0].strip().split(' ')
    t.weight = float(split[0][1:])
    t.name = split[1]
    
    top = True
    mem = 0
    start = False
    for i in range(len(treeline)):
        eachline = treeline[i]
        if eachline.find('(') == j:
            if eachline.find(')') > 0:
                if top: 
                    t.top = findweight(eachline)
                    top = False
                else:
                    t.bottom = findweight(eachline)
                    top = True
            else:
                start = True
                mem = i
        if eachline.find(')') == j and eachline.strip() == ')':
            childTree = createTree(treeline[mem: i+1])
            if top:
                t.top = childTree  
                top = False
            else:
                t.bottom = childTree
                top = True
            start = False
    #print treeline
    #print t.top, t.bottom
    return t
    
def calcCute(prob, tree, aniAttr):
    aprob = prob
    aprob *= tree.weight
    if tree.name == None:
        return aprob
    
    if tree.name in aniAttr:
        if isinstance(tree.top, Tree):
            aprob = calcCute(aprob, tree.top, aniAttr)
        else:
            aprob *= tree.top 
    else:
        if isinstance(tree.bottom, Tree):
            aprob = calcCute(aprob, tree.bottom, aniAttr)
        else:
            aprob *= tree.bottom
    return aprob

def process(casenum, casedata):
    #### CHANGE HERE ####
    tree, animals = casedata
    
    resultStr = '\n'
    for ani in animals:
        aniAttr = ani.split(' ')[2:]
        resultStr += '%.7f\n' % calcCute(1.0, tree, aniAttr)
        #print aniAttr
        
    return resultStr.rstrip()     
#    return i
    #### CHANGE HERE ####

if __name__ == '__main__':
    afile = file(filename)
    aread = afile.readlines()
    afile.close()
    
    out = file('out.txt', 'w')
    casefile = file('casefile.txt', 'w')
    
    #aread = [x.strip() for x in aread]
    
    numcase = int(aread[0])
    
    line = 1
    
    for i in range(1, numcase + 1):
        
        #### CHANGE HERE ####
        nt = int(aread[line])
        treeline = aread[line+1: line+1+nt]
        tree = createTree(treeline)
        aindex = line+1+nt
        na = int(aread[aindex])
        animals = aread[aindex + 1: aindex +1 + na]
        animals = [x.strip() for x in animals]
        #### CHANGE HERE ####
        #### CHANGE HERE ####
        #continue
        caseData = (tree, animals)
        tomove = nt + na + 2
        #### CHANGE HERE ####

        if False:
            print >> casefile, 'Case #%s' % i
            print >> casefile, '%s\n' % '\n'.join(aread[line: line + tomove])
            print >> casefile, '%s\n\n\n' % ('\n'.join([str(x) for x in caseData]))
        
        #### CHANGE HERE ####
        line += tomove
        #### CHANGE HERE
        result = process(i, caseData)
        #print 'result', result
        print >> out, 'Case #%s: %s' % (i,  result)
    
    casefile.close()
    out.close()
