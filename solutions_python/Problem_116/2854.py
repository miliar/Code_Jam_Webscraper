#!/usr/bin/env python2
import sys

def generate_situations(char):
    base = list(3*char)
    situations = []
    situations.append(''.join(4*char))
    for i in xrange(4):
        cpy = base[:]
        cpy.insert(i, "T")
        situations.append(''.join(cpy))
    return situations
        
x_win = generate_situations("X")
o_win = generate_situations("O")

win_situations = [x_win, o_win]
match = {
        0: "X won",
        1: "O won"
        }

def solve(board):
    def validate(board):
        lines = []
        #add rows
        lines += board
        #add cols
        for col in xrange(len(board)):
            line = []
            for row in xrange(len(board[col])):
                line.append(board[col][row])
            lines.append(''.join(line))
        #first diagonal
        line = []
        for x in xrange(len(board)):
            line.append(board[x][x])
        lines.append(''.join(line))

        line = []
        for x in xrange(4):
            y = -x+3
            line.append(board[y][x])
        lines.append(''.join(line))
        assert len(lines) == 10
        
        return filter(lambda l: '.' not in l, lines)  
            
    if not validate(board):
        return "Game has not completed"

    global win_situations
    global match

    for sit in xrange(len(win_situations)):
        #line-wise check
        for line in board:
            if line in win_situations[sit]:
                return match[sit]

        #column-wise check
        for col in xrange(len(board)):
            line = []
            for row in xrange(len(board)):
                line.append(board[row][col])
            if ''.join(line) in win_situations[sit]:
                return match[sit]

        #diagonal check
        line = []
        for x in xrange(len(board)):
            line.append(board[x][x])
        if ''.join(line) in win_situations[sit]:
            return match[sit]

        line = []
        for x in xrange(4):
            y = -x+3
            line.append(board[y][x])
        if ''.join(line) in win_situations[sit]:
            return match[sit]

    return "Draw"

with open(sys.argv[1]) as infile:
    cases = int(infile.readline().strip())
    board = []
    case_counter = 1
    row = 0
    for line in infile:
        if row < 4:
            board.append(line.strip())
            row += 1
        else:
            solution = solve(board)
            print "Case #%d: %s" % (case_counter, solution)
            case_counter += 1
            row = 0
            board = []
