#!/usr/bin/python

file = open('elso.txt', 'r')
cases = int(file.readline())

for i in range(0,cases):
    first = int(file.readline())
    a = []
    for j in range(1,5):
        l = file.readline().split()
        if first == j:
            a = l

    sec = int(file.readline())
    b = []
    for j in range(1,5):        
        l = file.readline().split()
        if sec == j:
            b = l
    
    same = set(a).intersection(set(b))
    result = len(list(same))
    magician = ""

    if result == 0:
        magician = "Volunteer cheated!"
    elif result > 1:
        magician = "Bad magician!"
    elif result == 1:
        magician = same.pop()

    
    print "Case #%d: %s" % (i+1,magician)
