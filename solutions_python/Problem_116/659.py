#!/usr/bin/python
import sys
#fd = open("A-small-attempt0.in", 'r')
fd = open("A-Large.in", 'r')
lines = fd.readlines()
#print lines[0]
num = int(lines[0])
curr = 1

def check (lst):
#    print "lst:", lst
    char = lst[0]
    if char == 'T':
        char = lst[1]
    won = True
    for i in range(0, 4):
        if lst[i] == '.':
            return 'U'
        elif lst[i] != 'T' and lst[i] != char:
            won = False
    if won:
        return char
    else:
        return 'F'

        


def scan (arr):
    finished = True
    arrs = [ 
            [arr[0][0], arr[0][1], arr[0][2], arr[0][3]],
            [arr[1][0], arr[1][1], arr[1][2], arr[1][3]],
            [arr[2][0], arr[2][1], arr[2][2], arr[2][3]],
            [arr[3][0], arr[3][1], arr[3][2], arr[3][3]],
            [arr[0][0], arr[1][0], arr[2][0], arr[3][0]],
            [arr[0][1], arr[1][1], arr[2][1], arr[3][1]],
            [arr[0][2], arr[1][2], arr[2][2], arr[3][2]],
            [arr[0][3], arr[1][3], arr[2][3], arr[3][3]],
            [arr[0][0], arr[1][1], arr[2][2], arr[3][3]],
            [arr[3][0], arr[2][1], arr[1][2], arr[0][3]],
            ]

    for idx in range (len(arrs)):
        res = check(arrs[idx])
        if res == 'X' or res == 'O':
            return res + " won"
        elif res == 'U':
            finished = False

    if finished:
        return 'Draw'
    else:
        return 'Game has not completed'


for idx in range(num):
    case_num = idx + 1
    arr = [
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            ]
    for i in range (curr, curr+4):
        line = lines[i].strip()
        for j in range(4):
#            print "j=", j, line[j], i-curr
            arr[i - curr][j] = line[j]
    res = scan (arr)
#    break    
    curr += 5
    print "Case #" + str(case_num) + ": "  + res
