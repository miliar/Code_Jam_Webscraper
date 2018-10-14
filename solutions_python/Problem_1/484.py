#!/usr/bin/python
import math
import sys
import time
import re

input = sys.argv[1]

d = open(input, 'r')
numOfTest = int(d.readline())

output = sys.argv[2]
out = open(output, 'w')

i = 0
while i < numOfTest:
    out.write("Case #")
    out.write(str(i+1))
    out.write(": ")

    switch = 0

    numOfMachine = int(d.readline())
    machines = range(numOfMachine)
    counts = range(numOfMachine)
    for count in range(numOfMachine) :
	machines[count] = d.readline()
	counts[count] = 0
  
    numOfUnusedMachine = numOfMachine
    numOfQuery = int(d.readline())
    for count in range(numOfQuery) :
	machine = d.readline()
	ind = machines.index(machine)
	if ind >= 0 :
	    if counts[ind] == 0 :
		counts[ind] = 1
		numOfUnusedMachine = numOfUnusedMachine - 1
		if numOfUnusedMachine == 0 :
		    switch = switch + 1
		    numOfUnusedMachine = numOfMachine - 1
		    for c in range(numOfMachine) :
			counts[c] = 0
		    counts[ind] = 1

    out.write(str(switch))
    out.write("\n")
    i = i + 1
