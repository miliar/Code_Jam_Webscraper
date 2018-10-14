#!/usr/bin/env python

import sys

input = [x.strip() for x in sys.stdin.xreadlines()]

lines = int(input[0])
input = input[1:]

for line in range(lines):
    params = input[line].split()
    snappers = int(params[0])
    switches = int(params[1])
    
    snapper_list = []
    for snapper in range(snappers):
        snapper_list.append(False)

    snapper_list_length = len(snapper_list)

#    print "length of snapper list: %d" % (snapper_list_length)
#    print "number of switches: %d" % (switches)

    for switch in range(switches):
        prev_snapper = True 
        for snapper in range(snapper_list_length):
            if prev_snapper:
                prev_snapper = snapper_list[snapper] 
                snapper_list[snapper] = not snapper_list[snapper] 

        #for snapper2 in range(snapper, snapper_list_length):
        #    if snapper_list[snapper2]:
        #        snapper_list[snapper2] = not snapper_list[snapper2]

    print "Case #%d: " % (line+1), 
    if all(snapper_list):
        print "ON" 
    else:
        print "OFF"

#0 0 0 0 0 0 0
#1 0 0 0 0 0 0
#0 1 0 0 0 0 0

