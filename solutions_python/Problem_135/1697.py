#!/usr/bin/python

f = open('input.in','r')
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

def solveCase(case_number, guess_1, arr_1, guess_2, arr_2):
    trial1Row = arr_1[guess_1 - 1]
    trial2Row = arr_2[guess_2 - 1]

    matches = set.intersection(set(trial1Row), set(trial2Row))
    output = 'Case #%d: ' % case_number
    if len(matches) == 0:
        output += 'Volunteer cheated!'
    elif len(matches) == 1:
        output += '%d' % list(matches)[0]
    else:
        output += 'Bad magician!'
    print output

testcases = parseInt()
case_number = 1
for testcase in xrange(testcases):
    # parse the input
    guess_1 = parseInt()
    t1_r0 = parseIntArray()
    t1_r1 = parseIntArray()
    t1_r2 = parseIntArray()
    t1_r3 = parseIntArray()
    arr_1 = [t1_r0,t1_r1,t1_r2,t1_r3]

    guess_2 = parseInt()
    t2_r0 = parseIntArray()
    t2_r1 = parseIntArray()
    t2_r2 = parseIntArray()
    t2_r3 = parseIntArray()
    arr_2 = [t2_r0,t2_r1,t2_r2,t2_r3]

    # determine the correct card
    solveCase(case_number, guess_1, arr_1, guess_2, arr_2)
    case_number += 1

    

