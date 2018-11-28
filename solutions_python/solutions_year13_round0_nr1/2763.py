#!/bin/python3
# -*- coding:utf-8 -*-


def whichwon(line1, line2, line3, line4):
    linelist = {line1, line2, line3, line4}
    
    linelistInv ={(line1[0], line2[0], line3[0], line4[0]),
                  (line1[1], line2[1], line3[1], line4[1]),
                  (line1[2], line2[2], line3[2], line4[2]),
                  (line1[3], line2[3], line3[3], line4[3]) }

    if(("X","X","X","X") in linelist or ("X","X","X","X") in linelistInv ):
        return "X won"

    triline = {(line1[0], line2[1], line3[2], line4[3]), (line1[3], line2[2], line3[1], line4[0])}
    
    if(("X","X","X","X") in triline ):
        return "X won"


    if(("O","O","O","O") in linelist or ("O","O","O","O") in linelistInv ):
        return "O won"


    if(("O","O","O","O") in triline ):
        return "O won"


    alllist = {line1[0], line2[0], line3[0], line4[0],
               line1[1], line2[1], line3[1], line4[1],
               line1[2], line2[2], line3[2], line4[2],
               line1[3], line2[3], line3[3], line4[3] }
    if( "." not in  alllist):
        return "Draw"

    return "Game has not completed"








filo = open('A-small-attempt1.in')
alllines = filo.readlines()
filo.close()

T = int(alllines[0])

#print(T, end="")

index = 1

for i in range(1, (5*T+1), 5):
    line1 = alllines[i].rstrip()
    line1 = line1.replace("T", "X")
    line1 = (line1[0], line1[1], line1[2], line1[3])
    
    line2 = alllines[i+1].rstrip()
    line2 = line2.replace("T", "X")
    line2 = (line2[0], line2[1], line2[2], line2[3])
    
    line3 = alllines[i+2].rstrip()
    line3 = line3.replace("T", "X")
    line3 = (line3[0], line3[1], line3[2], line3[3])
    
    line4 = alllines[i+3].rstrip()
    line4 = line4.replace("T", "X")
    line4 = (line4[0], line4[1], line4[2], line4[3])
    
    
    result1 = whichwon(line1, line2, line3, line4)
    
    line1 = alllines[i].rstrip()
    line1 = line1.replace("T", "O")
    line2 = alllines[i+1].rstrip()
    line2 = line2.replace("T", "O")
    line3 = alllines[i+2].rstrip()
    line3 = line3.replace("T", "O")
    line4 = alllines[i+3].rstrip()
    line4 = line4.replace("T", "O")
    result2 = whichwon(line1, line2, line3, line4)
    
    
    if(result1[0] != result2[0]):
        if(result1[0] == "X" ):
            result = result1
    
        if(result1[0] == "O"):
            result = result1
    else:
        result = result1

#    print("Case #" + str(index) + ": " + result1)
#    print("Case #" + str(index) + ": " + result2)
    
    print("Case #" + str(index) + ": " + result)
    
    index += 1



