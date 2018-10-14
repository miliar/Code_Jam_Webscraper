'''
Created on 2013-4-13

@author: Philip85517
'''

import sys

iHdler = open("A-large.in", "r")
oHdler = open("A-large.out", "w")
testCaseNum = int(iHdler.readline().strip())
board = []
sym_board = []


def check_line(line):
    cnt_empty = line.count('.')
    if cnt_empty > 0:
        return "N"
    cnt_T = line.count('T')
    cnt_X = line.count('X')
    cnt_O = line.count('O')
    
    if cnt_X + cnt_T == 4:
        return "X"
    if cnt_O + cnt_T == 4:
        return "O"
    
    return "D"

def get_ans(board):
    #check row
    left_diagnol = str()
    right_diagnol = str()
    empty_flag = False
    for i in range(0, 4):
        ret = check_line(board[i])
        if ret == "X":
            return "X won"
        if ret == "O":
            return "O won"
        if ret == "N":
            empty_flag = True
        left_diagnol += board[i][i]
        right_diagnol += board[i][3 - i]
    
    print left_diagnol
    print right_diagnol
    #check column
    column_line = str()
    for i in range(0, 4):
        column_line = ""
        for j in range(0, 4):
            column_line += board[j][i]
        ret = check_line(column_line)
        if ret == "X":
            return "X won"
        if ret == "O":
            return "O won"
        if ret == "N":
            empty_flag = True
    #check diagnol
    ret = check_line(left_diagnol)
    if ret == "X":
        return "X won"
    if ret == "O":
        return "O won"
    if ret == "N":
        empty_flag = True
    
    ret = check_line(right_diagnol)
    if ret == "X":
        return "X won"
    if ret == "O":
        return "O won"
    if ret == "N":
        empty_flag = True  
    
    if empty_flag == True:
        return "Game has not completed"
    else:
        return "Draw"

i = 0
board = list()
while i < testCaseNum:
    raw_line = iHdler.readline()

    if raw_line == "":
        break
    if raw_line == "\n":
        ans = get_ans(board)   
        oHdler.write("Case #%d: %s\n" % (i + 1, ans))
        i += 1
        board = list()
        continue
    board.append(raw_line.strip())

iHdler.close()
oHdler.close()
    