#!/usr/bin/python

f = open('input.in', 'rb')
t = f.readline()
input_data = f.readlines()
f.close()

pairs = 0
case = 1

for line in input_data:
	numrange = line.split()
	print numrange
	x = int(numrange[0])
	y = int(numrange[1])
	for n in range(x, y):
		for p in range(1, len(str(x))):
			if ( p >= len(str(x)) ) : break
			nstring = str(n)
			mstring = nstring[-p:] + nstring[0:len(str(x)) - p]
			if int(mstring) > int(nstring) and y >= int(mstring):
				pairs += 1
				print "%s : %s" % (nstring, mstring)

	print "Pairs: %d" % (pairs)

	f = open('output.out', 'ab')
	f.write("Case #%d: %s\n" % (case,pairs))
	case += 1
	f.close()

	pairs = 0

print "Done."
