#!/usr/bin/env python2.7

from sys import argv

script, filename = argv

inp = open(filename)

cases = int(inp.readline())
for num in range(0, cases):
    ans1 = int(inp.readline())
    arr = []
    for i in range(4):
        line = inp.readline()
        line = line.rstrip('\n').split(' ')
        line = [int(x) for x in line]
        arr.append(line)
    
    ans2 = int(inp.readline())
    arr2 = []
    for i in range(4):
        line = inp.readline()
        line = line.rstrip('\n').split(' ')
        line = [int(x) for x in line]
        arr2.append(line)

    first = arr[ans1 - 1]
    second = arr2[ans2 - 1]
    count = 0
    theNum = 0
    
    for i in first:
        for j in second:
            if i == j:
                count = count + 1
                #print i
                theNum = i
    
    if count == 0:
        print 'Case #%d: Volunteer cheated!' % (num + 1)
    elif count == 1:
        print 'Case #%d: %d' % (num + 1, theNum)
    elif count > 1:
        print 'Case #%d: Bad magician!' % (num + 1)
