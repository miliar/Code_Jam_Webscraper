#!/usr/bin/env python

import sys
import math

def readContent(fileName):
    with open(fileName, "r") as f_in:
        case = 0
        for line in f_in:
            line = line.strip()
            if len(line) == 4:
                caseStr += line
            else:
                if case > 0:
                    if len(caseStr) != 16:
                        sys.stderr.write("Opps, format is incorrect")
                        print(caseStr)
                    calculate(caseStr, case)
                    #print("Case #"+str(case),"\n",caseStr)
                case += 1
                caseStr = ""

def calculate(string, num):
    row = {}
    col = {}
    dia = {}
    for i in range(0,16,4):
        row[i] = string[i:i+4]
    for i in range(0,4):
        col[i] = string[i]+string[i+4]+string[i+8]+string[i+12]
    dia[1] = string[3]+string[6]+string[9]+string[12]
    dia[2] = string[0]+string[5]+string[10]+string[15]

    if check(row,num):
        return
    elif check(col,num):
        return
    elif check(dia,num):
        return
    elif "." in string:
        print("Case #"+str(num)+":", "Game has not completed")
    else:
        print("Case #"+str(num)+":", "Draw")

def check(theDict,num):
    for key, value in theDict.items():
        if 'T' in value:
            newValue = value.replace('T','');
            if newValue == newValue[0]*3:
                print("Case #"+str(num)+":",newValue[0], "won")
                return True
            else:
                continue
        else:
            if value[0] == value[1] == value[2] == value[3] and value[1] != '.':
                print("Case #"+str(num)+":",value[1], "won")
                return True
    return False


if __name__ == "__main__":
    assert len(sys.argv) < 3, "Too many arguments"
    readContent(sys.argv[1])
