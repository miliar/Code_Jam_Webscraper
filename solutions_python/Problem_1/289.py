import math
import re

fp = open('A-large.in.txt')

cases = int(fp.readline())

def someLeft(se):
    for k in se.keys():
        if se[k]:
            return True
    return False

def resetDict(se):
    for k in se.keys():
        se[k] = True
    return se

for case in range(0, cases):
    engineCount = int(fp.readline())
    se = {} # True = can still visit, false = can't visit
    for ec in range(0, engineCount):
        se[fp.readline().replace("\n", "")] = True
    
    queryCount = int(fp.readline())
    switch = 0
    for q in range(0, queryCount):
        query = fp.readline().replace("\n", "")
        se[query] = False
        if not someLeft(se):
            switch += 1
            resetDict(se)
            se[query] = False
    
    print "Case #%i: %i" % (case + 1, switch)

fp.close()
