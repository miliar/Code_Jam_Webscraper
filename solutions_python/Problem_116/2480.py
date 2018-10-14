#!/usr/bin/env python

def solve(board):
    #diagonal row wise and column wise
    #scan each row
    solutions = []
    rows = []
    cols = []
    diags = []
    for i in xrange(4):
        #[X, O, T, .]
        row = {'X':0, 'O':0, 'T':0,'.':0}
        col = {'X':0, 'O':0, 'T':0, '.':0}
        for j in xrange(4):
            #ROW
            row[board[i][j]] += 1
            col[board[j][i]] += 1

        if col['X'] + col['T'] == 4: return "X won"
        if col['O'] + col['T'] == 4: return "O won"
        if row['T'] + row['X'] == 4: return "X won"
        if row['T'] + row['O'] == 4: return "O won"
        rows.append(row)
        cols.append(cols)

    diag1 = {'X':0, 'O':0, 'T':0, '.':0}
    diag2 = {'X':0, 'O':0, 'T':0, '.':0}
    for i in xrange(4):
        diag1[board[i][i]] += 1
        diag2[board[i][3-i]] += 1

    if diag1['X'] + diag1['T'] == 4: return "X won"
    if diag2['X'] + diag2['T'] == 4: return "X won"
    if diag1['O'] + diag1['T'] == 4: return "O won"
    if diag2['O'] + diag2['T'] == 4: return "O won"

    diags.append(diag1)
    diags.append(diag2)
    #check if incomplete, if complete then draw, else Game has not completed
    dotCount = 0
    for row in rows:
        dotCount += row['.']
    if dotCount == 0: return "Draw"
    else: return "Game has not completed"

if __name__ == '__main__':
    T = input()
    board = [0 for i in xrange(4)]
    for i in xrange(T):
        for j in xrange(4):
            row_i = raw_input()
            board_row = [c for c in row_i]
            board[j] = row_i
        empty_line = raw_input()

        print "Case #%d: %s" % (i+1, solve(board))
