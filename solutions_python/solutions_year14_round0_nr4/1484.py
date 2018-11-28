#!/usr/bin/python
import sys

def find_next_largest(weights, target):
	for weight in weights:
		if weight > target:
			return weight
	return weights[0]



f = open(sys.argv[1], 'r')
inputs = f.read()
f2 = open("large_output", 'w')

lines = inputs.split('\n')
total_cases = int(lines[0])
for case in range(total_cases):
	naomi = [float(x) for x in lines[case*3+2].split(" ")]
	ken = [float(x) for x in lines[case*3+3].split(" ")]

	naomi.sort()
	ken.sort()

	#deceitful
	deceit = 0
	for block in ken:
		next_naomi = find_next_largest(naomi, block)
		if next_naomi > block:
			deceit += 1
			naomi.remove(next_naomi)
		else:
			break

	#reset the list
	normal = len(ken)
	naomi = [float(x) for x in lines[case*3+2].split(" ")]
	naomi.sort()

	for block in naomi:
		next_ken = find_next_largest(ken, block)
		if next_ken > block:
			normal -= 1
			ken.remove(next_ken)
		else:
			ken.remove(min(ken))

	f2.write("Case #%i: %i %i\n" % (case+1, deceit, normal))


