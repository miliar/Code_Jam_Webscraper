# -*- coding: utf-8 -*-
import fractions
import math

def printResult(i,result,outfile):
    print('Case #' + str(i + 1) + ': ' + result)
    outfile.write('Case #' + str(i + 1) + ': ' + result + '\n')

def getResult(remainderList,K) :
    if len(remainderList) < K and any(item == '-' for item in remainderList):
        return (0,'IMPOSSIBLE')
    elif len(remainderList) < K :
        return (0,'OK')
    elif remainderList[0] == '-' :
        newList = [item if idx >= K-1 else ('+' if item == '-' else '-') for idx,item in enumerate(remainderList[1:])];
        result = getResult(newList,K)
        return (result[0]+1,result[1])
    else :
        result = getResult(remainderList[1:], K)
        return (result[0],result[1])


fileName = 'A-small-attempt0.in'
with open(fileName, 'r') as infile, open(fileName + '_output.out', 'w') as outfile:
   
    T = int(infile.readline().split('\n')[0]);
    
    for i in range(0,T):

        line = infile.readline().split('\n')[0].split(' ');
        rows = list(line[0])
        K = int(line[1])

        result = getResult(rows,K)
        resstr = str(result[0]) if result[1] == 'OK' else 'IMPOSSIBLE';
        printResult(i, resstr, outfile);



        
    
    
    
