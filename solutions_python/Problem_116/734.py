#!/usr/bin/python
# -*- coding: utf-8 -*-

def winx(boardx):
    for r in xrange(4):
        if sum(boardx[r]) == 4:
            return True
        
    for c in xrange(4):
        score = 0
        for r in xrange(4):
            score = score + boardx[r][c]
        if score == 4:
            return True
        
    score1 = 0
    score2 = 0
    for d in xrange(4):
        score1 = score1 + boardx[d][d]
        score2 = score2 + boardx[d][3-d]
    
    if score1 == 4 or score2 == 4:
        return True;
        
    return False

def wino(boardo):
    for r in xrange(4):
        if sum(boardo[r]) == -4:
            return True
        
    for c in xrange(4):
        score = 0
        for r in xrange(4):
            score = score + boardo[r][c]
        if score == -4:
            return True
        
    score1 = 0
    score2 = 0
    for d in xrange(4):
        score1 = score1 + boardo[d][d]
        score2 = score2 + boardo[d][3-d]
    
    if score1 == -4 or score2 == -4:
        return True;
        
    return False

def haszero(board):
    for c in xrange(4):
        for r in xrange(4):
            if board[r][c] == 0:
                return True
        
    return False

def main():
    in_file = open("A-large.in", mode='r')
    out_file = open("A-large.out", mode='w')

    lines = in_file.readlines()      
    N = int(lines[0])
    
    # Convert the board to 1 and -1
    for i in xrange(N):
        board = lines[5*i+1:5*i+5]
        boardx = []
        boardo = []
        for row in board:
            rowx = []
            rowo = []
            for s in row[:-1]:
                if s=='X': 
                    rowx.append(1) 
                    rowo.append(1) 
                elif s=='O': 
                    rowx.append(-1) 
                    rowo.append(-1) 
                elif s=='T': 
                    rowx.append(1)
                    rowo.append(-1)
                else:
                    rowx.append(0)
                    rowo.append(0)
            boardx.append(rowx)
            boardo.append(rowo)
        
        if winx(boardx):
            out_file.write("Case #" + str(i+1) +": X won\n")
        elif wino(boardo):
            out_file.write("Case #" + str(i+1) +": O won\n")
        elif haszero(boardx) or haszero(boardo):
            out_file.write("Case #" + str(i+1) +": Game has not completed\n")
        else:
            out_file.write("Case #" + str(i+1) +": Draw\n")
        
    in_file.close()
    out_file.close()

if __name__ == '__main__':
    main()