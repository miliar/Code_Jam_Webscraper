'''
Created on 11 apr 2015

@author: algestam
'''

def solve(x, r, c):
    #print x, r, c
    if x > r*c:
        return "RICHARD"
    if not (r*c) % x == 0:
        return "RICHARD"
    if x == 3:
        if r*c == 3:
            return "RICHARD"
    if x == 4:
        if r*c == 4 or r*c == 8:
            return "RICHARD"
    
    return "GABRIEL"
    

for case in xrange(input()):
    X, R, C = [int(c) for c in raw_input().split()]
    
    res = solve(X, R, C)

    print "Case #%i: %s" % (case+1, res)