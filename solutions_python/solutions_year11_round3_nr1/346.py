#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
input = sys.stdin
output = sys.stdout

IMPOSSIBLE = 'Impossible'
BLUE = '#'

def row_has_no_blue(r):
    return all(map(lambda c: c!=BLUE, r))

def solve(R,C,rows):
    
    NOTHING = (False,[])

    for i in range(R):
        rows[i] = list(rows[i])

    if R<2 or C<2:
        no_blue = all(map(row_has_no_blue,rows))
        if no_blue:
            return True,rows
        else:
            return NOTHING
    
    for i in range(R-1):
        j=0
        while (j<C-1):
            c = rows[i][j]
            if c==BLUE:
                # try to place tile
                if ((rows[i+1][j] != BLUE) 
                    or (rows[i][j+1] != BLUE) 
                    or (rows[i+1][j+1] != BLUE)):
                    return NOTHING
                else:
                    rows[i][j] = '/'
                    rows[i+1][j] = '\\'
                    rows[i][j+1] = '\\'
                    rows[i+1][j+1] = '/'
                    j += 2
            else:
                j += 1
                
        if rows[i][C-1]==BLUE:
            return NOTHING

    if row_has_no_blue(rows[R-1]):
        return True,rows
    else:
        return NOTHING

T = int(input.readline())
assert 1<=T and T<=50

for t in range(1,T+1):
    S = input.readline().split(' ')
    R = int(S[0])
    C = int(S[1])
    assert 1<=R and R<=50
    assert 1<=C and C<=50
    
    rows = []
    for i in range(R):
        rs = input.readline().strip()
        assert len(rs) == C
        rows.append(rs)
    
    possible,redrows = solve(R,C,rows)
    
    output.write('Case #%s:\n' % (str(t)))
    
    if not possible:
        output.write('%s' % IMPOSSIBLE)
        if t<T:
            output.write('\n')
    else:
        for i in range(R):
            r = redrows[i]
            rs = ''.join(r)
            output.write('%s' % rs)
            if t<T or i<R-1:
                output.write('\n')
