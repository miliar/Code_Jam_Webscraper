#!/usr/bin/python

filename = map(str.rstrip, open("A-small.in", 'r').readlines())
output = open("A-small.out", 'w')
t = int(filename[0])
inputs = [(int(x.split(' ')[0]), int(x.split(' ')[1])) for x in filename[1:]]
for i, x in enumerate(inputs):
	if (x[1]+1)%(2**x[0]) == 0:
		print >>output, "Case #" + str(i+1) + ":", "ON"
	else:
		print >>output, "Case #" + str(i+1) + ":", "OFF"
output.close()

