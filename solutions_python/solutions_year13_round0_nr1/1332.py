#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      qmarchal
#
# Created:     11/04/2013
# Copyright:   (c) qmarchal 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
f = open("A-large.in")
T = int(f.readline())

def writeOutput(output):
    w = open("ouput.txt","w")
    w.write(output)
    w.close()
def nextInt():
    return int(f.readline())
def nextList():
    return f.readline().split()
def nextIntList():
    strings = f.readline().split()
    ints = []
    for string in strings:
        ints.append(int(string))
    return ints
def nextStr():
    return f.readline()
def main():
    output = "";
    for t in range(1,T+1,1):
        output +="Case #%d: "%t + case() + "\n"
    writeOutput(output)
def case():
    output = ""
    N = 4
    table = []
    xwon = False
    owon = False
    for n in range (0,N,1):
        table.append(nextStr().replace("\n",""))
    string=""
    for line in table:
        string+="|"+line+"|"
    for i in range(0,4,1):
        for j in range(0,4,1):
            string+=table[j][i]
        string+="|"
    for i in range(0,4,1):
        string+=table[i][i]
    string+="|"
    for i in range(0,4,1):
        string+=table[3-i][i]
    if "XXXX" in string.replace("T","X"):
        xwon = True
    if "OOOO" in string.replace("T","O"):
        owon = True
    trash=nextStr()
    if (xwon):
        output+="X won"
    elif (owon):
        output+="O won"
    else:
        end = True
        for line in table:
            if ("." in line):
                output+="Game has not completed"
                end = False
                break
        if (end):
            output+="Draw"
    return output
if __name__ == '__main__':
    main()
