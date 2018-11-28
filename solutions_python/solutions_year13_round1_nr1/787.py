from time import sleep
import math

def amount(radius):
	return (1 + (radius * 2))

lines = [line.strip() for line in open('input.txt')]
cases = int(lines[0])
lines.pop(0)
outfile = open('output.txt', 'w')

i = 0
for line in lines:
	i += 1
	values = line.split()
	radius = int(values[0])
	paint  = int(values[1])

	rings = 0
	taken = amount(radius)
	while taken <= paint:
		paint = paint - taken
		rings += 1
		radius += 2
		taken = amount(radius)

	outfile.write("Case #"+str(i)+": "+str(rings)+"\n")
