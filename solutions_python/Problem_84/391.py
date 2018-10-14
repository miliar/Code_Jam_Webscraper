#-------------------------------------------------------------------------------
# Name:        A-small-0.py
# Purpose:     Google Code Jam
#
# Author:      Jakub Koba
#
# Created:     07-05-2011
# Copyright:   (c) Jakub Koba 2011
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sys


def resolve_case(case,counter):
    red_tile = ["/","\\","\\","/"]
    red_tile.reverse()
    imp_string = ""

    for i,row in enumerate(case):
        for r,el in enumerate(row):
            if el == "#":
                try:
                    if case[i][r+1] =="#" and case[i+1][r] == "#" and case[i+1][r+1]:
                        case[i][r] = red_tile.pop()
                        case[i][r+1] = red_tile.pop()
                        case[i+1][r] = red_tile.pop()
                        case[i+1][r+1] = red_tile.pop()
                        red_tile = ["/","\\","\\","/"]
                    else:
                        imp_string = "Impossible"
                except:
                    imp_string = "Impossible"
    print "Case #"+str(counter) + ":"
    if imp_string != "":
        print imp_string
    else:
        for row in case:
            s = ""
            print s.join(row)


def main():
    f = open(sys.argv[1])
    #f = open("A-large.in")
    c_count=f.readline()
    for caseNum in range(int(c_count)):
        conf=f.readline()
        row_count,col_count=conf.split(" ")
        row_count=int(row_count)
        col_count=int(col_count)
        case = []

        for rowNum in range(int(row_count)):
            rowStr = f.readline().rstrip()

            row=[]
            case.insert(rowNum,row)
            for el in rowStr:
                case[rowNum].append(el)

        resolve_case(case,caseNum+1)

if __name__ == '__main__':
    main()
