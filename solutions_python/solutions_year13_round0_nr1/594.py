#! /usr/bin/python

__author__ = 'Thomas "noio" van den Berg'

### IMPORTS ###
import sys
import numpy as np
from pprint import pprint


### FUNCTIONS ###    

def do(field):
    pprint(field)
    field = np.array(field)
    X = field == 'X'
    O = field == 'O'
    T = field == 'T'
    E = field == '.'
    XT = X + T
    OT = O + T
    
    if any(all(row) for row in XT):
        return 'X won'
    if any(all(row) for row in XT.T):
        return 'X won'
    if all(np.diag(XT)):
        return 'X won'
    if all(np.diag(np.fliplr(XT))):
        return 'X won'

    if all(np.diag(OT)):
        return 'O won'
    if all(np.diag(np.fliplr(OT))):
        return 'O won'
    if any(all(row) for row in OT):
        return 'O won'
    if any(all(row) for row in OT.T):
        return 'O won'

    
    if any(any(r) for r in E):
        return "Game has not completed"
    return "Draw"

### PROCESS INPUT FILE ###

if __name__ == '__main__':
    f = open(sys.argv[1])
    fout = open(sys.argv[1].replace('.in','.out'),'w')

    T = int(f.readline())
    for case in xrange(T):
        field = [list(f.readline().strip()) for _ in xrange(4)]
        ans = do
        f.readline()
        
        ans = do(field)
        print ans
        fout.write('Case #%d: %s\n'%(case+1,ans))
