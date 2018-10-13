#!/usr/bin/python

T = int(raw_input())
count = 1

while T != 0:
    r1 = int(raw_input())
    for i in xrange(1,5):
        if i == r1:
            list1 = raw_input().strip().split()
        else:
            null = raw_input()
        if i == 4:
            break

    r2 = int(raw_input())
    for i in xrange(1,5):
        if i == r2:
            list2 = raw_input().strip().split()
        else:
            null = raw_input()
        if i == 4:
            break
    
    common = [x for x in list1 if x in list2]
    
    if len(common) == 0:
        print "Case #" + str(count) + ": " + "Volunteer cheated!"
    elif len(common) > 1:
        print "Case #" + str(count) + ": " + "Bad magician!"
    elif len(common) == 1:
        print "Case #" + str(count) + ": " + str(int(common[0]))

    T = T - 1
    count = count + 1

