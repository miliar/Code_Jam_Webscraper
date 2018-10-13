# -*- coding: utf-8 -*-

'''
Created on 2010/05/08

@author: Keniya
'''

import copy

def solve(R,K,q):
    Money = 0;
    while R:
        wkK = K
        wkQ = copy.copy(q)
        for grp in q:
            wkK -= grp
            if wkK < 0: break
            Money += grp
            wkQ.pop(0)
            wkQ.append(grp)
        q = copy.copy(wkQ)
        R -= 1
        
    return Money

def main(filen):
    answers = []
    
    file = open(filen)
    firstLine = True
    paramLine = True
    R,K = 0,0
    q = []
    for line in file:
        if firstLine:
            firstLine = False
            continue
        if paramLine:
            R = int(line.split(" ")[0])
            K = int(line.split(" ")[1])
            paramLine = False
            continue
        q = [int(x) for x in line.split(" ")]
        answers.append(solve(R,K,q))
        paramLine = True
        
    file.close()
    
    file = open( filen.replace("attempt","answer").replace(".in",".txt"), "w")
    i = 0;
    for ans in answers:
        i += 1
        file.write("Case #" + str(i) + ": " + str(ans) + "\n" )
    file.close()
    

#print solve(4,6,[1,4,2,1])
#print solve(100,10,[1])
#print solve(5,5,[2,4,2,3,4,2,1,2,1,3])

filen = "C:\\temp\\C-small-attempt0.in";
main(filen)


'''
3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3

Case #1: 21
Case #2: 100
Case #3: 20

'''
