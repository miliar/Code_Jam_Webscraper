#!/usr/bin/python

f = open('input','r')
lines = f.readlines()
l = 0

def parseInt():
    global lines, l
    val = int(lines[l].strip())
    l += 1
    return val

def parseIntArray():
    global lines, l
    val = [ int(x) for x in lines[l].strip().split(' ') ]
    l += 1
    return val

def parseFloatArray():
    global lines, l
    val = [ float(x) for x in lines[l].strip().split(' ') ]
    l += 1
    return val

######################################################################
######################################################################
######################################################################
def getTime(nfactories, factory_cost, factory_production, winning_score):
    'buy n factories, and then wait until you win'
    rate = 2.0
    elapsed = 0.0
    score = 0.0

    # time spent purchasing factories
    purchased_factories = 0
    while purchased_factories < nfactories:
        elapsed += factory_cost / rate
        rate += factory_production
        purchased_factories += 1

    # time spent capitalizing
    elapsed += winning_score / rate
    return elapsed

def solveCase(case_number, factory_cost, factory_production, winning_score):
    output = 'Case #%d: ' % case_number

    best_time = getTime(0, factory_cost, factory_production, winning_score)
    best_nfactories = 0
    i = 1
    while True:
        time = getTime(i, factory_cost, factory_production, winning_score)
        if time >= best_time:
            break
        best_time = time
        best_nfactories = i
        i += 1

    output += '%.7f' % best_time
    print output

testcases = parseInt()
case_number = 1
for testcase in xrange(testcases):
    # parse the input
    cost, production, winning_score = parseFloatArray()

    # determine the correct card
    solveCase(case_number, cost, production, winning_score)
    case_number += 1



