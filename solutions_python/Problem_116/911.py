'''
Created on Apr 8, 2013

@author: kon
'''
import template
import numpy as np

def does_win(st, inp, rinp):
    win = False
    s1 = st*4
    s2 = ''.join(sorted('T' + st*3))
    for el in inp.view('S4').tolist():
        sti = ''.join(sorted(el[0]))
        if sti == s1:
            win = True
            break
        elif sti == s2:
            win = True
            break
    if not win:
        for el in rinp.view('S4').tolist():
            sti = ''.join(sorted(el[0]))
            if sti == s1:
                win = True
                break
            elif sti == s2:
                win = True
                break
    if not win:
        sti = ''.join(sorted(inp.diagonal(0)))
        if sti == s1:
            win = True
        elif sti == s2:
            win = True
        sti = ''.join(sorted(rinp.diagonal(0)))
        if sti == s1:
            win = True
        elif sti == s2:
            win = True
    return win

def solve(f):
    T = int(f.readline())
    res = []
    for _ in range(T):
        inp = np.array(['.']*4*4,dtype='S1')
        inp = np.resize(inp, (4,4))
        fullboard = True
        for i in range(4):
            l = f.readline().strip()
            for j,c in enumerate(l):
                if c!='.':
                    inp[i,j] = c
                else:
                    fullboard = False
        f.readline()
        rotinp = np.resize(np.rot90(inp), (4, 4))
        isXwin = does_win('X', inp, rotinp)
        isOwin = does_win('O', inp, rotinp)
        if isXwin:
            res.append('X won')
        elif isOwin:
            res.append('O won')
        elif fullboard:
            res.append('Draw')
        else:
            res.append('Game has not completed')

    return res

if __name__ == '__main__':
    template.solve("A-large.in", solve)