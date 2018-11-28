import re
import string
from collections import Counter

root = r"C:/Python27/Mine/codejam/"

#these are not needed
#BASES = set(("Q", "W", "E", "R", "A", "S", "D", "F"))
#CONTINGENT = set((c for c in string.ascii_uppercase if not c in BASES))

def solve(fname,outname = "A-small.out"):
    infile = open(root + fname,'rU')
    outfile = open(root + outname,'w')
    return solve_inner(infile,outfile)

def solve_inner(infile,outfile):
    casesline = infile.readline()
    cases = int(casesline)
    for case in xrange(1,cases + 1):
        instructionsline = infile.readline()
        instructionset = instructionsline.strip().split(" ")
        instructionset.reverse()
        sets = []
        for setNum in xrange(2):
            numInSet = int(instructionset.pop())
            theSet = []
            for i in xrange(numInSet):
                theSet.append(instructionset.pop())
            sets.append(theSet)
        instructionset.pop()
        sets.append(instructionset.pop())
        if case > 1:
            outfile.write("\n")
        outfile.write("Case #%s: %s" % (case,processCase(sets)))
    return True

def processCase(sets):
    combinersInput, destructorsInput, operations = sets
    operations = iter(operations)
    combiners = processToDict(combinersInput)
    destructors = processToOtherDict(destructorsInput)
    potentialDestructors = Counter()
    reagents = []
    for operation in operations:
        reagents.append(operation)
        if operation in destructors:
            potentialDestructors.update(operation)
        lastAdded = operation
        while len(reagents) >= 2: #combination phase
            lastTwo = tuple(sorted(reagents[-2:]))
            if lastTwo in combiners:
                for r in lastTwo:
                    oldR = potentialDestructors[r]
                    if oldR <= 1:
                        del potentialDestructors[r]
                    else:
                        potentialDestructors[r] = oldR - 1
                reagents.pop()
                reagents.pop()
                lastAdded = combiners[lastTwo]
                reagents.append(lastAdded)
            else:
                break
        if len(reagents) >= 2: #destruction phase
            if lastAdded in destructors:
                opposedBy = destructors[lastAdded]
                for potential in opposedBy:
                    if potentialDestructors[potential] > 0: #bang
                        reagents = []
                        potentialDestructors.clear()
    return "[" + ', '.join(reagents) + "]"

def processToDict(inlist):
    out = dict()
    for element in inlist:
        args, result = element[:2], element[2]
        out[tuple(sorted(args))] = result
    return out

def processToOtherDict(inlist):
    out = dict()
    for element in inlist:
        for first, second in [(element[0],element[1]),(element[1],element[0])]:
            if first in out:
                out[first].append(second)
            else:
                out[first] = [second]
    return out
