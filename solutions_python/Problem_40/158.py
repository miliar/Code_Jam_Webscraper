#!/usr/bin/env python
"""google code jam : Round 1B"""


import sys, re

def find_closing_bracket(text, start) :
    bl = 1
    i = start 
    while bl > 0 :
        i = i + 1
        if text[i] == '(' :
            bl = bl + 1
        if text[i] == ')' :
            bl = bl - 1 
    return i

def buildTree(tB) :
    """ tB tree lines blended into 1. (0.2 furry (0.81 fast (0.3)(0.2))(0.1 fishy (0.3 freshwater (0.01) (0.01)) (0.1) ))
    recusive function.@"""
    #print(tB)
    if tB.find('(',1) == -1 :
        if tB.find('(') == -1 :
            return float(tB)
        else :
            return float(tB[1:-1])
    else :
        pB = tB.find('(',1)
        #print(tB[1:pB])
        p_t, p_f = tB[1:pB-1].split(' ') 
        p1 = find_closing_bracket(tB,pB)
        p2 = tB.find('(',p1)
        p3 = find_closing_bracket(tB,p2)
        return [float(p_t), p_f, buildTree(tB[pB+1:p1]),buildTree(tB[p2+1:p3]) ]

def analyse_Animal(tree, animal):
    P = 1.0
    aFeature = animal[2:len(animal)]
    #print(animal,aFeature)
    def walkTree(p,cL) :
        pS = cL[0]
        if any([cL[1] == aF for aF in aFeature]) :
            if type(cL[2]) == float :
                return p*pS*cL[2]
            else :
                return walkTree(p*pS,cL[2])
        else :
            if type(cL[3]) == float :
                return p*pS*cL[3]
            else :
                return walkTree(p*pS,cL[3])
    return walkTree(1.0,tree)

def analyse_datafile(datafile):
    f = file(datafile)
    lines = f.readlines()
    f.close()
    N = int(lines[0].strip())
    print('file "%s" contains cases %i' % (datafile,N))
    i = 1 
    trees = []
    animalC = []
    for j in range(N) :
        T = int(lines[i].strip())
        textRaw = " ".join([ln.strip() for ln in lines[i+1:i+T+1]])
        print textRaw
        trees.append(buildTree(textRaw))
        print trees[-1]
        i2 = i+T+1
        A = int(lines[i2].strip())
        animals = []
        for j in range(A) :
            aA = lines[i2+j+1].strip().split(' ') #animal desciption
            animals.append(aA)
        i = i2 + A + 1
        print animals
        animalC.append(animals)
    output = []
    count = 1
    for T,A in zip(trees,animalC):
        output.append('Case #%i:'%count)
        print output[-1]
        print(T)
        count = count + 1
        for ani in A :
            if type(T) <> float :
                output.append("%9.7f" % (analyse_Animal(T,ani)))
            else :
                output.append("%9.7f" % (T))
            print output[-1]

    return output


output =  analyse_datafile(sys.argv[1])

fout = file(sys.argv[1]+'_output','w')
fout.write('\n'.join(output))
fout.close()
