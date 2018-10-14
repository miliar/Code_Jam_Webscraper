#!/usr/bin/python

import sys

'''
 y in combiners[x].keys() iff x and y combine with each other
 if y in combiners[x].keys() then x and y combine to give combiners[x][y]
 Also y in combiners[x].keys() iff x in combiners[y].keys()
 And if y in combiners[x].keys() then combiners[x][y]=combiners[y][x]
'''
combiners={}

''' 
 y in opposers[x].keys() iff x and y oppose each other
 and y in opposers[x].keys() iff x in opposers[y].keys()
'''
opposers={}

def simplify(l1,l2,str1):
    combiners={}
    opposers={}

    for x in l1:
        if not x[0] in combiners:
            combiners[x[0]]={}
        combiners[x[0]][x[1]] = x[2]
        if not x[1] in combiners:
            combiners[x[1]]={}
        combiners[x[1]][x[0]] = x[2]

    for x in l2:
        if not x[0] in opposers:
            opposers[x[0]]={}
        opposers[x[0]][x[1]] = ""
        if not x[1] in opposers:
            opposers[x[1]]={}
        opposers[x[1]][x[0]] = ""
        
#    print combiners
#    print opposers
        
    opp  = []
    expr = []

    for cChar in str1:
        if len(expr) > 0:
            pChar = expr[-1]

        if expr == []:
            expr = [cChar]
        elif (pChar in combiners) and (cChar in combiners[pChar]):
            expr[-1] = combiners[pChar][cChar]
        else:
            if pChar in opposers:
                opp += opposers[pChar].keys()
            if cChar in opp:
                opp =[]
                expr=[]
            else :
                expr.append(cChar)
 
    return expr

tests = int(sys.stdin.readline())
t=0
while(t<tests):
    inList = (sys.stdin.readline()).split()

    n      = int(inList[0])
    inList = inList[1:]
    l1     = inList[0:n]
    inList = inList[n:]

    n      = int(inList[0])
    inList = inList[1:]
    l2     = inList[0:n]    
    inList = inList[n:]
    
    inString = inList[1]
 #   print "inString : "+inString
    expr   = simplify(l1,l2,inString)
    
    exprStr="["
    i,n = 1,len(expr)
    if(n>0):    exprStr += expr[0]
    while i < n:
        exprStr += ", "+expr[i]
        i+=1        
    exprStr+="]"

    print "Case #"+str(t+1)+": "+exprStr
    t+=1
