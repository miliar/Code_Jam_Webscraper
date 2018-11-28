#!/usr/bin/python

import sys


def ReadN(fp):
    line = fp.readline()
    N = int(line)
    return N

def ReadBoard(fp):
    board = []
    for x in xrange(4):
        line = fp.readline()
        line = line.strip()
        board.append(line)
    # skip one empty
    fp.readline()
    return board


def CheckWin(tL):
    tL.sort()
    if tL[0]=='.':
        return ['.',False]  # not complete yet
    elif tL[0]=='O' and tL[-1]!='X':
        return ['O',True]  # O win
    elif tL[0]=='X' or tL[0]=='T':
        return ['X',True]  # X win
    else:
        return ['T',False] # draw

def CheckBoard(board):
    # check horizontal
    empty = False
    for line in board:
        [win, flag] = CheckWin(list(line))
        if flag:
            return win
        elif win=='.':
            empty = True
    # check vertical
    for i in xrange(4):
        tL = [line[i] for line in board]
        [win, flag] = CheckWin(tL)
        if flag:
            return win
        elif win=='.':
            empty = True
    # check dialog
    tL = [board[i][i] for i in range(4)]
    [win, flag] = CheckWin(tL)
    if flag:
        return win
    elif win=='.':
        empty = True
    tL = [board[i][3-i] for i in range(4)]
    [win, flag] = CheckWin(tL)
    if flag:
        return win
    elif win=='.':
        empty = True

    if empty:
        return '.'
    else:
        return 'T'
    

def Test(fname):
    fp = open(fname,'r')
    res = open(fname[:-4]+"_res.txt","wt")
    N = ReadN(fp) 
    for i in xrange(N):
        print "case ", i
        board = ReadBoard(fp)
        win = CheckBoard(board)
        if win=='X':
            ans = "X won"
        elif win=='O':
            ans = "O won"
        elif win=='.':
            ans = "Game has not completed"
        else:
            ans = "Draw"
        print ans
        resL = "Case #%d: %s\n" %(i+1,ans)
        res.write(resL)

    fp.close()
    res.close()
    print "done."


if __name__=="__main__":
    if len(sys.argv)<2:
        print "please input the test file"
        sys.exit()
    fname = sys.argv[1]
    Test(fname)
