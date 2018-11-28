#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
    	line = raw_input().split(' ')
    	max_shyness = line[0]
    	li = line[1]
    	standing = 0
    	invite = 0
    	level= 0
    	for s in li:
    		if standing >= level:
    			standing += int(s)
    		else:
    			invite += level - standing
    			standing = level + int(s)  			
    		level += 1

    	print("Case #%i: %i" % (caseNr, invite))
   	