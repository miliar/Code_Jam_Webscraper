#!/usr/bin/env python
# encoding: utf

def parse_array(fileDescriptor):
    f = fileDescriptor

    n = int(f.readline())
    array = map(lambda x: int(x), f.readline().split(' '))

    return array

def solve_case(array):
    # Let's assume Goro knows which elements are on their right positions, so
    # Goro locks that numbers and hit the others, every hit locks a new number
    orderedArray = array[:]
    orderedArray.sort()

    notLocked = 0
    for i in xrange(len(array)):
        if orderedArray[i] != array[i]:
            notLocked += 1

    return notLocked

def solve(filename):
    f = open(filename, "r")
    fsol = open("solution.txt", "w")

    t = int(f.readline())
    for i in xrange(t):
        array = parse_array(f)
        r = solve_case(array)
        fsol.write("Case #%d: %f\n" %(i+1, float(r)))
