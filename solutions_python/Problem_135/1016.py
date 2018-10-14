# -*- coding: utf-8 -*-

f = open("A-small-attempt0.in")
T = int(f.readline())

for t in range(T):
    a = int(f.readline())
    for i in range(1, 5):
        s = f.readline()
        if i == a:
            firstset = set(map(int, s.split(" ")))
    b = int(f.readline())
    for i in range(1, 5):
        s = f.readline()
        if i == b:
            secondset = set(map(int, s.split(" ")))
    dup = firstset & secondset
    
    print "Case #%d:" %(t+1),
    if len(dup) == 0:
        print "Volunteer cheated!"
    elif len(dup) == 1:
        print dup.pop()
    else:
        print "Bad magician!"
        
        