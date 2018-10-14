from itertools import chain
from pprint import pprint
import sys
IN = sys.stdin
cases = int(IN.readline())


def cols(b):
    for i in xrange(len(b[0])):
        yield col(b, i)
def col(b, i):
    for row in b:
        yield row[i]
def rows(b):
    for r in b:
        yield r
def diags(b, n, k):
    br = list(b)
    br.reverse()
    
    yield diag(b, n, 0, 0)
    yield diag(br, n, 0, 0)
    for i in xrange(1, n-k+1):
        yield diag(b, n, 0, i)
        yield diag(b, n, i, 0)
        yield diag(br, n, 0, i)
        yield diag(br, n, i, 0)
def diag(b, n, i, j):
    while i<n and j<n:
        yield b[i][j]
        i+=1
        j+=1
def wins(line, k):
    rflag = False
    bflag = False
    red = 0
    blue = 0
    for c in line:
        if c == 'R':
            red += 1
            blue = 0
        elif c == 'B':
            blue += 1
            red = 0
        rflag |= red >= k
        bflag |= blue >= k
    return rflag, bflag
for casenum in xrange(1,cases+1):
    board = []
    s = IN.readline().split()
    n, k = map(int, s)
    row = []
    for i in xrange(n):
        row = IN.readline().strip()
        row = row.replace(".", "")
        row = "." * (n - len(row)) + row
        row = list(row)
        row.reverse()
        board.append(row)
    
    redWins = False
    blueWins = False
    
    for line in chain(rows(board), cols(board), diags(board, n, k)):
        r, b = wins(line, k)
        redWins |= r
        blueWins |= b
    
    print "Case #%d:" % casenum,
    if redWins:
        if blueWins:
            print "Both"
        else:
            print "Red"
    elif blueWins:
        print "Blue"
    else:
        print "Neither"