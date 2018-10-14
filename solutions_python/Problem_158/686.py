__author__ = 'lowikchanussot'

def solveX1(r, c) :
    return True #Gabriel Wins all the time

def solveX2(r, c) :
    """ Gabriel wins if R*C is multiple of 2"""
    return ((r*c)%2 == 0)

def solveX3(r, c) :
    if(r < c) : r, c = c, r
    if r*c %3 != 0 : return False
    if r*c < 6 : return False
    if c < 2 : return False # choose the one corner 3-omino
    return True

def solveX4(r, c) :
    if(r < c) : r, c = c, r
    if r*c%4 != 0 : return False
    if r*c <= 4: return False
    if c <= 2 : return False #choose 4-omino with S-form
    return True

def solve(x, r, c):
    if x == 1: return solveX1(r, c)
    elif x == 2: return solveX2(r, c)
    elif x == 3: return solveX3(r, c)
    elif x == 4: return solveX4(r, c)
    print 'Error'

def solveD(input, output) :
    with open(input, 'r') as inp, open(output, 'w') as out :
        lines = inp.readlines()
        for i, line in enumerate(lines[1:]):
            tok = line.split()
            x, r, c = int(tok[0]), int(tok[1]), int(tok[2])
            sol = solve(x, r, c)
            if sol :
                out.write("Case #%d: GABRIEL\n"%(i+1))
            else :
                out.write("Case #%d: RICHARD\n"%(i+1))

if __name__ == '__main__':
    import sys
    import os
    _, input = sys.argv
    output = os.path.splitext(input)[0] + '.out'
    solveD(input, output)