'''
Created on 13 apr. 2013

@author: Peter
'''

cases = int(raw_input())

def solve(x, y, lines):
    for i in xrange(x):
        for j in xrange(y):
            value = lines[i][j]
            if any(lines[ii][j] > value for ii in xrange(x)) and\
                any(lines[i][jj] > value for jj in xrange(y)):
                return 'NO'
    return 'YES'
    
    
for case in xrange(1, cases + 1):
    x, y = raw_input().split()
    x = int(x)
    y = int(y)
    lines = []
    for _ in xrange(x):
        lines.append(raw_input().strip().replace(" ", ""))    
    
    print "Case #%s: %s" % (case, solve(x, y, lines))
