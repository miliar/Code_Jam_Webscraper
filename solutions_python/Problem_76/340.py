import re
import string
from collections import Counter

root = r"C:/Python27/Mine/codejam/"

def solve(fname,outname = "A-small.out"):
    infile = open(root + fname,'rU')
    outfile = open(root + outname,'w')
    return solve_inner(infile,outfile)

def solve_inner(infile,outfile):
    casesline = infile.readline()
    cases = int(casesline)
    for case in xrange(1,cases + 1):
        infile.readline() #junked
        instructionsline = infile.readline()
        instructionset = instructionsline.strip().split(" ")
        candies = [int(ci) for ci in instructionset[:]]
        if case > 1:
            outfile.write("\n")
        outfile.write("Case #%s: %s" % (case,processCase(candies)))
    return True

def processCase(candies):
    total = 0
    lowest = -1
    xor = 0
    for c in candies:
        total += c
        xor ^= c
        if lowest < 0 or lowest > c:
            lowest = c
    if xor == 0: #otherwise impossible
        #since patAdd(ordered) = 0 and patAdd(0) = 0, we already have equal amounts
        #but we need non-empty piles, so we simply take the lowest from Sean's and give it to Pat
        #which gives patAdd(Sean) = lowest and patAdd(Pat) = lowest, since XOR behaves as both addition and subtraction
        return total - lowest
    return "NO"

def patAdd(inlist): #not used
    return reduce(lambda a,b:a ^ b,inlist,0)
