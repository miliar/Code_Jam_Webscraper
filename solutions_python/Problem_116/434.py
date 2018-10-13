#!/usr/bin/env python

import sys
import re
# row, col, diag r-l, diag l-r
Xwin = re.compile("""  ^(....)*(X|T){4}
                       | ((X|T)...){3}(X|T)
                       | ((X|T)..){3}(X|T)...$
                       | ^((X|T)....){3}(X|T)      """, re.X)

Owin = re.compile("""  ^(....)*(O|T){4}
                       | ((O|T)...){3}(O|T)
                       | ((O|T)..){3}(O|T)...$
                       | ^((O|T)....){3}(O|T)      """, re.X)

Qempty = re.compile("\.")

f = open(sys.argv[1], 'r')

T = int(f.readline())
for i in range(T):
    board = ''
    for j in range(4):
        l = f.readline().strip()
        board += l
    l = f.readline().strip()

    if Xwin.search(board):
        r = "X won"
    elif Owin.search(board):
        r = "O won"
    elif Qempty.search(board):
        r = "Game has not completed"
    else:
        r = "Draw"

    print "Case #%d: %s" % (i+1, r)
f.close()
