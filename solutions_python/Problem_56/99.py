#
# Google Code Jam 2010
# Roaund 1A: A. Rotate
# submission by EnTerr
#

import sys
import re

f = open(sys.argv[1])
def input(): return f.readline().strip();

def check(board, N, K, c):
    # check if there are K number of char c lined up
    return bool(
        re.search('%c{%d}' % (c, K), board) 
        or re.search('%c(.{%d}%c){%d}' % (c, N, c, K-1), board) 
        or re.search('%c(.{%d}%c){%d}' % (c, N-1, c, K-1), board) 
        or re.search('%c(.{%d}%c){%d}' % (c, N+1, c, K-1), board) 
    )

for caseNo in xrange(1, int(input())+1):
    (N, K) = map(int, input().split())
    # read rows and slide them to the right
    board = '|'.join([input().replace('.','').zfill(N) for i in range(N)])
    print 'Case #%d: %s' % (caseNo, ['Neither','Red','Blue','Both'][2 * check(board, N, K, 'B') + check(board, N, K, 'R')])

