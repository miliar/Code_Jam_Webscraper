import os
import sys

def runcase(line):
    def makekey(key):
        if key[0]>key[1]:
            key=key[1]+key[0]

        return key
 
    parts = line.split(" ")
    combcount = int(parts.pop(0))
    combs = dict()
    for i in range(0,combcount):
        item = parts.pop(0)
        key = makekey(item[0:2])
        combs[key] = item[2]

    opposecount = int(parts.pop(0))
    opposes = []
    for i in range(0,opposecount): 
        key = makekey(parts.pop(0))
        opposes.append(key)

    outitems =[]

    chars = parts[1]
    for c in chars:
        if len(outitems) > 0:
            key = makekey(c+outitems[-1])
            if key in combs:
                outitems.pop(-1)
                outitems.append(combs[key])
                continue
        for c2 in outitems:
            if makekey(c+c2) in opposes:
                outitems = []
                break
        else:
            outitems.append(c)

    return '[%s]' % (', '.join(outitems))

def run():
    count = int(sys.stdin.readline().strip())
    for i in range(0,count):
        print('Case #%d: %s' % (i+1,runcase(sys.stdin.readline().strip())))

run()
