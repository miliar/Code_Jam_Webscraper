#!/bin/python

f = open('A-small-attempt2.in')

testcases = int(f.readline())
#print testcases

for i in range (testcases):
    n = int(f.readline())
    #print "N: ", n
    for j in range(n-1):
        s = f.readline()
        #print "Skipped 1: " , s
    numbers = f.readline().strip().split(' ')
    #print i+1, " -> ", numbers
    for j in range (4-n):
        s = f.readline()
        #print "Skipped 2: ", s
    m = int(f.readline())
    #print "M: ", m
    for j in range(m-1):
        s = f.readline()
        #print "Skipped 1: " , s
    numbers2 = f.readline().strip().split(' ')
    #print i+1, " -> ", numbers
    for j in range (4-m):
        s = f.readline()
        #print "Skipped 2: ", s
    first = None
    second = False
    for a in numbers:
        for b in numbers2:
            if a == b:
                if first is not None:
                    second = True
                    break
                first = a
        if second:
            break
    if second:
        print "Case #%d: Bad magician!" % int(i+1)
    elif first:
        print "Case #%d: %s" % (i+1, first)
    if not first:
        print "Case #%d: Volunteer cheated!" % int(i+1)

