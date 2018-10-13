#!/usr/bin/env python

in_file = open('input.txt','r')

count_exec = int(in_file.readline().strip())

def checkOrder(x):
    y = -1
    for x in str(x):
        if int(x) < y:
            return False
        y = int(x)
    return True

for x in range(0,count_exec):
    in_var = int(in_file.readline().strip())
    while not checkOrder(in_var):
        in_var -= 1
    print "Case #%d: %d" % (x+1,in_var)
