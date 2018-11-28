from __future__ import absolute_import, division, print_function

import sys

def solveCase():
    incomplete = False
    lines = [sys.stdin.readline().strip() for _ in range(4)]
    sys.stdin.readline()
    # horizontal
    for line in lines:
        incomplete = incomplete or ('.' in line)
        winner = 'T'
        for c in line:
            if c == '.': break
            if c == 'T': continue
            if winner == 'T': winner = c
            elif winner != c: break
        else:
            return winner + ' won'
    # vertical
    for j in range(4):
        winner = 'T'
        for i in range(4):
            c = lines[i][j]
            if c == '.': break
            if c == 'T': continue
            if winner == 'T': winner = c
            elif winner != c: break
        else:
            return winner + ' won'
    # \ diagonal
    winner = 'T'
    for i in range(4):
        c = lines[i][i]
        if c == '.': break
        if c == 'T': continue
        if winner == 'T': winner = c
        elif winner != c: break
    else:
        return winner + ' won'
    # / diagonal
    winner = 'T'
    for i in range(4):
        c = lines[i][3-i]
        if c == '.': break
        if c == 'T': continue
        if winner == 'T': winner = c
        elif winner != c: break
    else:
        return winner + ' won'
    # Incomplete / Draw
    return incomplete and "Game has not completed" or "Draw"

if __name__ == "__main__":
    for i in range(1, 1+int(sys.stdin.readline().strip())):
        print('Case #', i, ': ', solveCase(), sep='', end='\n')
