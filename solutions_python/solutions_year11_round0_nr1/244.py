#!/usr/bin/env python
# encoding: utf-8

import os

def parse_sequence(fileDescriptor):
    # Returns a sequence to complete
    f = fileDescriptor
    sequence = f.readline()

    sequence = sequence.split(' ')
    n = int(sequence[0])
    sequence_a = []
    sequence_b = []
    sequence_r = []

    have_color = False
    last_color = 'O'
    for i in xrange(1,len(sequence)):
        if not have_color and (sequence[i] == 'O' or sequence[i] == 'B'):
            have_color = True
            last_color = sequence[i]
        elif have_color and (sequence[i] != 'O' and sequence[i] != 'B'):
            t = (int(sequence[i]), last_color)
            if t[1] == 'O':
                sequence_a.append(t)
            else:
                sequence_b.append(t)
            sequence_r.append(t)
            have_color = False
        else:
            print "Badformed Input"
            exit()

    return n, sequence_r, sequence_a, sequence_b

def min_time(n, sequence, seqO, seqB):
    posO = 1
    posB = 1
    cTime = 0

    for step in sequence:
        if step[1] == 'O':
            toComplete = timeToComplete(posO, step[0])
            cTime += toComplete
            posO = step[0]
            seqO.pop(0)

            if seqB:
                # Is not empty
                posB = newPosition(posB, seqB[0][0], toComplete)
        else:
            toComplete = timeToComplete(posB, step[0])
            cTime += toComplete
            posB = step[0]
            seqB.pop(0)

            if seqO:
                # Is not empty
                posO = newPosition(posO, seqO[0][0], toComplete)

    return cTime

def timeToComplete(currPos, destPos):
    return (max(currPos, destPos) - min(currPos, destPos) + 1)

def newPosition(currPos, destPos, time):
    result = 0
    advance = min(timeToComplete(currPos, destPos) -1, time)
    if currPos < destPos:
        result = currPos + advance
    else:
        result = currPos - advance

    return result

def solve(fileName):
    try:
        f = open(fileName, "r")
    except:
        exit()

    test_cases = int(f.readline())

    for i in xrange(test_cases):
        args = parse_sequence(f)
        result = min_time(*args)
        print "Case #%d: %d" %(i+1, result)
