#!/usr/bin/env python
# Google CodeJam Assignment A

def robotsQualify(candy):
    ret = 'NO'
    if not xor(candy):
        ret = sum(candy)-min(candy)

    return ret

def parseInput(f):
    f.readline() #not needed
    commandList = f.readline().split()
    candy = [int(c) for c in commandList]
    return candy
    

def xor(l):
    t = 0
    for i in l:
        t ^= i
    return t

if __name__ == "__main__":
    mainfn = robotsQualify

    import sys
    if len(sys.argv)==1:
        filename = 'test.in'
    else:
        filename = sys.argv[1]

    f = open(filename)
    line = f.readline()
    for case in range(int(line)):
        args = parseInput(f)
        print "Case #%i: %s" % (case+1, mainfn(args))
