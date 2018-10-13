from __future__ import division
from fractions import Fraction
from math import ceil

root = r"C:/Python27/Mine/codejam/"

def solve(fname,outname = "A-small.out"):
    infile = open(root + fname,'rU')
    outfile = open(root + outname,'w')
    return solve_inner(infile,outfile)

def solve_inner(infile,outfile):
    casesline = infile.readline()
    cases = int(casesline)
    for case in xrange(1,cases + 1):
        R, C = [int(rc) for rc in infile.readline().strip().split()]
        args = []
        for r in xrange(R):
            args.append([k == "#" for k in infile.readline().strip()])
        if case > 1:
            outfile.write("\n")
        outfile.write("Case #%s:\n%s" % (case,processCase(args)))
    return True

def processCase(args):
    result = processInner(args)
    if not result:
        return "Impossible"
    return result

def processInner(args):
    bluesLeft = 0
    reds = []
    for row in args:
        redRow = []
        for k in row:
            if k:
                bluesLeft += 1
            redRow.append(".")
        reds.append(redRow)
    if bluesLeft % 4 != 0:
        return False #obviously need a multiple of 4 tiles
    bluesLeft //= 4
    HEIGHT = len(args)
    WIDTH = len(args[0])
    smallIsBlue = lambda x,y:isBlue(x,y,args,WIDTH,HEIGHT)
    while bluesLeft:
        modified = False
        for y,row in enumerate(args[:-1]):
            for x,tile in enumerate(row[:-1]):
                if smallIsBlue(x,y) and smallIsBlue(x + 1,y) and smallIsBlue(x,y + 1) and smallIsBlue(x + 1,y + 1):
                    redded = False
                    if not smallIsBlue(x - 1,y) and not smallIsBlue(x,y - 1):
                        redded = True
                    elif not smallIsBlue(x - 1,y + 1) and not smallIsBlue(x,y + 2):
                        redded = True
                    elif not smallIsBlue(x + 2,y) and not smallIsBlue(x + 1,y - 1):
                        redded = True
                    elif not smallIsBlue(x + 2,y + 1) and not smallIsBlue(x + 1,y + 2):
                        redded = True
                    if redded:
                        bluesLeft -= 1
                        redise(args,reds,x,y)
                        modified = True
        if not modified:
            return False #couldn't make any headway
    return "\n".join(["".join(r) for r in reds])

def isBlue(x,y,args,width,height):
    if x < 0 or x >= width:
        return False
    if y < 0 or y >= height:
        return False
    return args[y][x]

def redise(args,reds,x,y):
    args[y][x] = False
    args[y + 1][x] = False
    args[y + 1][x + 1] = False
    args[y][x + 1] = False
    reds[y][x] = "/"
    reds[y + 1][x + 1] = "/"
    reds[y + 1][x] = "\\"
    reds[y][x + 1] = "\\"
