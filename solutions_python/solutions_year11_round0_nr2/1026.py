
from copy import copy
import numpy as np



def parseLine(line):

    tokens = line.split()

    ncomb = int(tokens[0])
    comb = tokens[1:ncomb+1]
    tokens = tokens[ncomb+1:]

    nopp = int(tokens[0])
    opp = tokens[1:nopp+1]
    tokens = tokens[nopp+1:]

    for c in copy(opp):
        opp.append(c[::-1])

    assert len(tokens) == 2, "Error parsing input string"
    ninv = int(tokens[0])
    invoked = tokens[1]

    combDict = {}
    for c in comb:
        combDict[ c[:-1] ] = c[-1]
        combDict[ c[:-1][::-1] ] = c[-1]

    #print combDict, opp, invoked
    return combDict, opp, invoked

def invoke(combinations, opposed, invoked):

    elem = []
    for c in invoked:
        if not len(elem):
            elem.append(c)
        else:
            comb = elem[-1]+c
            if comb in combinations:
                elem[-1] = combinations[comb]
            else:
                elem.append(c)

            newcombs = [elem[-1] + e for e in elem[:-1]]
            if len( np.intersect1d_nu(newcombs, opposed) ):
                elem = []

    return elem


fin = file("B-small-0.in")
#fin = file("B-small-example.in")
ncase = int(fin.readline().strip())

fout = file ("B-small-0.out", "w")


for i, line in enumerate(fin):
    print line
    comb, opposed, invoked = parseLine( line.strip() )

    elements = invoke(comb, opposed, invoked)

    outStr = "Case #%i: [%s]" % (i+1, ", ".join(map(str, elements)))
    print outStr
    fout.write(outStr + "\n")

fout.close()

