#!/usr/bin/env python
#-*- coding:utf-8 -*-

board = "OOOT....OO......"

def main():
    raw_input() # Dummy line
    
    case = 1

    while True:
        board = ""
        pref = "Case #%d: " % case
        try:   
            for i in xrange(0, 5 ):
                board += raw_input()
        except:
            break
        
        out = check(board.replace("T", "X"))
        if out is not None:
            print pref + out
        else:
            out = check(board.replace("T", "O"))
            if out is not None:
                print pref + out
            elif "." in board:
                print pref + "Game has not completed"
            else:
                print pref + "Draw"
        
        case += 1

def check(b):
    """
    checks if anyone won
    """
    # Check rows
    for i in xrange(0, 4):
        r = b[i*4:i*4+4]
        if row(r):
            return row(r)
            
    # Check columns
    for i in xrange(0, 4):
        c = [b[j+i] for j in range(0, 16, 4)]
        if row(c):
            return row(c)
    
    # Check diagonals
    d1 = [b[0], b[5], b[10], b[15]]
    d2 = [b[3], b[6], b[9], b[12]]
    
    if row(d1):
        return row(d1)
    if row(d2): 
        return row(d2)
    
def row(li):
    """
    check if a row is all equal
    returns False or the symbol repeated in the row
    """
    li = "".join(li)
    if li == "XXXX":
        return "X won"
    elif li == "OOOO":
        return "O won"
    else:
        return False

if __name__ == '__main__':
    main()


