#!/usr/bin/python
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

import fileinput



t = int(input())
#print("numLines = %d" % (t))
caseNum = 1
for line in fileinput.input():
    if caseNum > t:
        break;

    stringA, stringLength = line.split(" ")
    K = int(stringLength);
    listA = list(stringA);
    S = len(listA);
    finPos = S-K;
    totalFlips = 0;
    possible = True;
    
    for curPos in range(finPos + 1):
        if (listA[curPos] is "-"):
            for i in range(curPos, curPos+K):
                if listA[i] is "-":
                    listA[i] = "+"
                else:
                    listA[i] = "-"

            totalFlips+=1;

    for curPos in range(finPos + 1, S):
        if (listA[curPos] is "-"):
            possible=False;
            break;
    
    if possible:
        print("Case #%d: %d" % (caseNum, totalFlips))
    else:
        print("Case #%d: IMPOSSIBLE" % (caseNum))
    caseNum+=1;

        
    
    
            
        
        
    
            
            
        
    
    

        
        

  
