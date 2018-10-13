#!/usr/bin/env python

input_file = open('input.txt','r')

case_count = int(input_file.readline().strip())

for x in range(0,case_count):
    (pancake_stack,flipper) = tuple(input_file.readline().split(' '))
    flipper = int(flipper)
    flips = 0
    for y in range(0,len(pancake_stack)+1-flipper):
        if pancake_stack[y] is '-':
            pancake_stack = pancake_stack[0:y] + pancake_stack[y:flipper+y].replace('-','0').replace('+','-').replace('0','+') + pancake_stack[y+flipper:len(pancake_stack)]
            flips+=1
    if '-' in pancake_stack:
        print "Case #%d: IMPOSSIBLE" % (x+1)
        continue
    print "Case #%d: %d" % (x+1,flips)
