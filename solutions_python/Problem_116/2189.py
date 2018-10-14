#!/usr/bin/python

import sys

def main():    
    f = open(sys.argv[1]).read().splitlines()
    i=0
    no_input = int(f[i])
    count = 0
    mat = ['A','B','C','D']
    while count < no_input:
        count = count + 1
        mat[0] = f[(count - 1) * 5 + 1]
        mat[1] = f[(count - 1) * 5 + 2]
        mat[2] = f[(count - 1) * 5 + 3]
        mat[3] = f[(count - 1) * 5 + 4]
        zipped = zip(*mat)
        # print mat
        res = cal_row(mat)
        if res != 'N':
            print "Case #" + str(count) + ": " + str(res) + " won"
            continue

        res = cal_row(zipped)
        if res != 'N':
            print "Case #" +  str(count) + ": " + str(res) + " won"
            continue

        res = cal_diag(mat)
        if res != 'N':
            print "Case #" +  str(count) + ": " + str(res) + " won"
            continue

        res = cal_draw(mat)
        if res == 1:
            print "Case #" +  str(count) + ": " + "Game has not completed"
        else:
            print "Case #" +  str(count) + ": " + "Draw"

def cal_row(a):
    for a1 in a:
        no_x = 0
        no_O = 0
        no_T = 0
        for a2 in a1:
            if a2 == 'X':
                no_x = no_x + 1
            elif a2 == 'O':
                no_O = no_O + 1
            elif a2 == 'T':
                no_T = no_T + 1
        if no_T + no_x == 4:
            return "X"
        if no_T + no_O == 4:
            return "O"
    return 'N'

def cal_diag(a):
    i=0
    no_x = 0
    no_O = 0
    no_T = 0
    for a1 in a:
        if a1[i] == 'X':
                no_x = no_x + 1
        elif a1[i] == 'O':
                no_O = no_O + 1
        elif a1[i] == 'T':
                no_T = no_T + 1
        i = i + 1
    if no_T + no_x == 4:
        return "X"
    if no_T + no_O == 4:
        return "O"

    i=3
    no_x = 0
    no_O = 0
    no_T = 0
    for a1 in a:
        if a1[i] == 'X':
                no_x = no_x + 1
        elif a1[i] == 'O':
                no_O = no_O + 1
        elif a1[i] == 'T':
                no_T = no_T + 1
        i = i - 1
    if no_T + no_x == 4:
        return "X"
    if no_T + no_O == 4:
        return "O"
    
    return 'N'

def cal_draw(a):
    for a1 in a:
        for a2 in a1:
            if a2 == ".":
                return 1
    return 0

if __name__=='__main__':
    main()
