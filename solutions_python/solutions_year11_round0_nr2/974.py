#!/usr/bin/python

import sys

def process(line):
    line = line.strip()
    items = line.split(" ")
    c = int(items[0])
    combines = items[1:c+1]
    d = int(items[c+1])
    combinations = {}
    for tmp in combines:
        combinations[tmp[0:2]] = tmp[2]
        combinations["%s%s" % (tmp[1], tmp[0])] = tmp[2]
    opposeds = items[c+2:d+c+2]
    opposings = {}
    for a, b in opposeds:
        if a not in opposings:
            opposings[a] = []
        opposings[a].append(b)
        if b not in opposings:
            opposings[b] = []
        opposings[b].append(a)
    n = int(items[d+c+2])
    seque = items[d+c+3]

    # handle sequence
    target = []
    clearListCandidates = []
    last = None
    lastsCLC = []
    for s in seque:
        zz = "%s%s" % (last, s)
        if zz in combinations:
            target.append(combinations[zz])
            last = None
            lastsCLC = []
        elif s in clearListCandidates or s in lastsCLC:
            target = []
            clearListCandidates = []
            last = None
            lastsCLC = []
        else:
            if last is not None:
                target.append(last)
                for tmp in lastsCLC:
                    clearListCandidates.append(tmp)
            last = s
            lastsCLC = []
            if s in opposings:
                for t in opposings[s]:
                    lastsCLC.append(t)
    if last is not None:
        target.append(last)
    return target


def ltostr(x):
    return ", ".join(x)

if __name__ == '__main__':
    i = 0
    for line in sys.stdin.readlines():
        if i == 0:
            nrOfTestCases = int(line)
        else:
            x = process(line)
            y = ltostr(x)
            print "Case #%d: [%s]" % (i, y)
        i += 1
