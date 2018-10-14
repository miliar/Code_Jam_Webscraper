#!/usr/bin/python

import sys
import re

rcds = [slice(0,4,None), slice(4,8,None), slice(8,12,None), slice(12,16,None),
        slice(0,None,4), slice(1,None,4), slice(2,None,4), slice(3,None,4),
        slice(0,None,5), slice(3,-1,3)
        ]

T = int(next(sys.stdin))

for case in xrange(1,T+1):
    board = ''.join(next(sys.stdin).strip() for _ in xrange(4))
    if '.' in board:
        result = 'Game has not completed'
    else:
        result = 'Draw'
    for s in rcds:
        if re.search(r'^[XT]+$', board[s]):
            result = 'X won'
            break
        elif re.search(r'^[OT]+$', board[s]):
            result = 'O won'
            break
    print "Case #%d: %s" % (case, result)
    try:
        next(sys.stdin)
    except:
        pass
