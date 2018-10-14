#!/usr/bin/python
import math

fd = open('input.txt','r')
count = int(fd.readline().strip())
iterator = 0
while iterator < count:
    iterator += 1
    output = 0
    a,b = (int(x) for x in fd.readline().strip().split(" "))
    for x in range(a,b+1):
        if (math.sqrt(x) % 1):
            continue
        possible = list(str(int(math.sqrt(x))))
        original = list(str(int(x)))
        if len(possible) % 1:
            possible.pop(len(possible)/2)
        if len(original) % 1:
            original.pop(len(original)/2)
        flag = False
        for y in range(0,len(possible)/2):
            if possible[y] is not possible[-(y+1)]:
                flag = True
        for y in range(0,len(original)/2):
            if original[y] is not original[-(y+1)]:
                flag = True
        if flag:
            continue
        output += 1
    # Tell us what you found
    output = "Case #%s: %s" % (iterator,output)
    print output
