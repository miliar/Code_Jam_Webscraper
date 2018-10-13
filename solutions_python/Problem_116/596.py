
import sys
import numpy as np
import pandas as pd
    
horz_slices = [slice(x,x+4) for x in 4*np.arange(4)]
vert_slices = [slice(x,None,4) for x in np.arange(4)]
diag_idx_1 = [x*4+x for x in range(4)]
diag_idx_2 = [(x+1)*4-(x+1) for x in range(4)]

UNCM = -1
DRAW = 0
XWIN = 1
OWIN = 2

res_to_str = {UNCM: 'Game has not completed',
              DRAW: 'Draw',
              XWIN: 'X won',
              OWIN: 'O won'}

def no_empty_spaces(game):
    if '.' not in game:
        return True
    else:
        return False

def all_are(chars, char):
    return reduce(lambda x,y: x and y, map(lambda x: x is char or x is 'T', chars), 'True')

def winner(chars):
    if '.' in chars:
        return UNCM
    if all_are(chars, 'X'):
        return XWIN
    if all_are(chars, 'O'):
        return OWIN
    return UNCM


def horz_win(game):
    horz_strs = map(lambda x: game[x], horz_slices)
    for horz_str in horz_strs:
        winstr = winner(horz_str)
        if winstr is not UNCM:
            return winstr
    return winstr
            
def vert_win(game):
    vert_strs = map(lambda x: game[x], vert_slices)
    for vert_str in vert_strs:
        winstr = winner(vert_str)
        if winstr is not UNCM:
            return winstr
    return winstr

def diag_win(game):
    diag1 = map(lambda x: game[x], diag_idx_1)
    diag2 = map(lambda x: game[x], diag_idx_2)
    diag1win = winner(diag1)
    if diag1win is not UNCM:
        return diag1win
    diag2win = winner(diag2)
    if diag2win is not UNCM:
        return diag2win
    return diag2win

def check_game(game):
    hwin = horz_win(game)
    if hwin is not UNCM: return hwin
    vwin = vert_win(game)
    if vwin is not UNCM: return vwin
    dwin = diag_win(game)
    if dwin is not UNCM: return dwin
    if no_empty_spaces(game): return DRAW
    return UNCM


############################
# Begin parse of inputfile #
############################

if __name__ == '__main__':

    infile = open(sys.argv[1], 'rb')
    lines = map(lambda x: x.rstrip(), infile.readlines())

    N = int(lines[0])  # Number of cases
    lineIdx = 1
    caseNo = 1

    while (lineIdx < len(lines)):
        gamelines = map(lambda x: x.rstrip(), lines[lineIdx:lineIdx+4])
        game = ''.join(gamelines)
        caseAnswer = res_to_str[ check_game(game) ]
        print 'Case #%d: %s' % (caseNo, caseAnswer)
        lineIdx += 5
        caseNo += 1
    


