import numpy as np
import os
import re

def main():
    infile = "Asmall.in"
    inf = open(infile, 'r')

    outfile = "Asmall.out"
    outf = open(outfile, 'w')

    lnum = 0
    case = 0
    totcase = 0
    for line in inf:
        if (lnum == 0):
            totcase = int(line.split()[0])
            string1 = ''
            string2 = ''
            row1 = 0
            row2 = 0
            answer = 0
        elif (lnum % 10 == 1):
            row1 = int(line.split()[0])
        elif (lnum % 10 == 6):
            row2 = int(line.split()[0])
        elif (row1 != 0 and lnum % 10 == row1 + 1):
            string1 = line
        elif (row2 != 0 and lnum % 10 == (row2 + 6) % 10):
            string2 = line
        if (lnum % 10 == 0 and lnum != 0) :
            case += 1
            s1 = string1.split()
            s2 = string2.split()
            for i in range(16):
                s1flag = 0
                s2flag = 0
                for j in range(len(s1)):
                    if (str(i+1) == s1[j]):
                        s1flag = 1
                    if (str(i+1) == s2[j]):
                        s2flag = 1
                if (s1flag and s2flag):
                    if (answer == 0):
                        answer = str(i + 1)
                    else :
                        answer = 'Bad magician!'
            if (answer == 0):
                answer = 'Volunteer cheated!'
            outf.write("Case #" + str(case) + ": " + answer + "\n")
            string1 = ''
            string2 = ''
            row1 = 0
            row2 = 0
            answer = 0
        lnum += 1
            


if __name__ == '__main__':
     main()
