#!/usr/bin/python

def solveCase(index, a, b):
	b = b + 1
	a = 2 ** a
	if b % a == 0:
		state = "ON"
	else:
		state = "OFF"
	return "Case #%i: %s" % (index, state)

input = open("/Users/george/Downloads/A-large.in", "rU").read()

input = input.split("\n")[1:]

i = 0
output = ""
for line in input:
	if line != "":
		(a, b) = line.split(" ")
		i += 1
		output += solveCase(i, int(a), int(b)) + "\n"

o = open("/Users/george/Desktop/output", "w")
o.write(output)
o.close()