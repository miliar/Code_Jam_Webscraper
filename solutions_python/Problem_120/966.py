# Round 1A : Problem A

import sys
import os
import math

def ReadInput(filename):
	if not os.path.exists(filename):
	   sys.exit('ERROR: could not open input file')

	f = open(filename,'r')

	items = []

	count = int(f.readline())

	for i in range(count):
		stemp = f.readline()
		if len(stemp) == 0:
			break # EOF
		items.append(stemp.split())

	f.close()

	if count != len(items):
		sys.exit('ERROR: only found %d/%d items' % (len(items),count))

	return items

def MaximumBlackRings(r,t):
    count = 0
    cr = int(r) + 1
    cp = int(t)

    while( True ):
    	delta = cr+cr-1
    	cr += 2
    	
    	if delta <= cp:
    		cp -= delta
    		count += 1
    	else:
    		break
    return count

# main script

if len(sys.argv) < 2:
	print "   usage: <input> <output>"
	sys.exit(-1)

filename = sys.argv[1]
outputFile = sys.argv[2]

f = open(outputFile,'w')

dataItems = ReadInput(filename)
for i in range(len(dataItems)):
	f.write("Case #%s: %d" % (i+1, MaximumBlackRings(dataItems[i][0], dataItems[i][1])))
	f.write('\n')

f.close()