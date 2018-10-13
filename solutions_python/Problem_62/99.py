#!/usr/bin/env python
# Google CodeJam Round 1C-A

def main(wires):
	crosses = 0
	for i, wire in enumerate(wires[:-1]):
		for wire2 in wires[i+1:]:
			if wire[0]<wire2[0] and wire[1]>wire2[1]:
				crosses+=1
			if wire[0]>wire2[0] and wire[1]<wire2[1]:
				crosses+=1
	return crosses

if __name__ == "__main__":
	prog = main
	import sys
	for filename in sys.argv[1:]:
		f = open(filename)
		line = f.readline()
		for case in range(int(line)):
			wires = []
			for amountofwires in range(int(f.readline())):
				wires.append(tuple([int(value) for value in f.readline().split()[:3]]))
			print "Case #%i: %s" % (case+1, prog(wires))