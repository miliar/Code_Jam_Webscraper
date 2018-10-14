#!/usr/bin/python


import sys
from itertools import izip


def check_player(sign, rows):
    mod_rows = map(lambda r: ''.join(sign if c == 'T' else c for c in r), rows)
    
    goal = ''.join(sign for _ in xrange(4))
    
    # TODO: randomize order to speed it up?
    
    for row in mod_rows:
        if row == goal:
            return True
    
    for i in xrange(4):
        if ''.join(r[i] for r in mod_rows) == goal:
            return True
    
    if ''.join(r[i] for r, i in izip(mod_rows, xrange(4))) == goal:
        return True
    
    if ''.join(r[i] for r, i in izip(mod_rows, xrange(3,-1,-1))) == goal:
        return True
    
    return False


def check_board(rows):
    # TODO: randomize order to speed it up?
    
    if check_player('O', rows):
        return "O won"
    if check_player('X', rows):
        return "X won"
    
    if '.' in ''.join(row for row in rows):
        return "Game has not completed"
    
    return "Draw"


def main():
    fin_file = sys.argv[1]
    
    with open(fin_file, 'r') as fin:
        T = int(fin.readline().strip())
        
        for t in xrange(T):
            rows = []
            
            for _ in xrange(4):
                rows.append(fin.readline().strip())
            
            fin.readline()
            
            print "Case #%d: %s" % ((t + 1), check_board(rows))

        
if __name__ == '__main__':
    main()
    