#!/usr/bin/python
import math

fd = open('input.txt','r')
count = int(fd.readline().strip())
iterator = 0
while iterator < count:
    iterator += 1
    result = -1
    pickRow = int(fd.readline().strip())
    for x in range(0,pickRow):
        firstNumbers = [int(y) for y in fd.readline().strip().split(" ")]
    for x in range(pickRow,4):
        throwaway = fd.readline()
    pickRow = int(fd.readline().strip())
    for x in range(0,pickRow):
        secondNumbers = [int(y) for y in fd.readline().strip().split(" ")]
    for x in range(pickRow,4):
        throwaway = fd.readline()
    for x in firstNumbers:
        if x in secondNumbers:
            if result is -1:
                result = x
            else:
                result = 0
    if result is -1:
        output = "Case #%s: Volunteer cheated!" % (iterator)
    elif result is 0:
        output = "Case #%s: Bad magician!" % (iterator)
    elif result:
        output = "Case #%s: %s" % (iterator,result)
    print output