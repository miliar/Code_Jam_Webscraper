#!/usr/bin/python
import sys

def not_surprising(total):
    r = total % 3
    if r == 0:
        return total / 3
    elif r == 1:
        return (total+2) / 3
    else:
        return (total+1) / 3

def surprising(total):
    r = total % 3
    if r == 0:
        best = (total+3) / 3
    elif r == 1:
        best = (total+2) / 3
    else:
        best = (total+4) / 3
    if total == 0:
        best = 0
    elif total == 29 or total == 30:
        best = 10
    return best

def cal(surprices, p, scores):
    result = 0
    for score in scores:
        if not_surprising(score) >= p:
            result += 1
            continue
        if surprising(score) >= p and surprices > 0:
            result += 1
            surprices -= 1
            continue
    return result

cases = sys.stdin.readline()
n = int(cases)
for i in xrange(1, n+1):
    line = sys.stdin.readline()
    fields = line.split()
    people = int(fields[0])
    surprices = int(fields[1])
    p = int(fields[2])
    scores = [int(x) for x in fields[3:]]
    print "Case #%d: %d" % (i, cal(surprices, p, scores))
