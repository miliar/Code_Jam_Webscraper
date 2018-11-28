import sys

def solve(input):
	i = 0
	
	coms = input[i+1:i+1+int(input[i])]
	i += int(input[i]) + 1
	opps = input[i+1:i+1+int(input[i])]
	i += int(input[i]) + 1
	puzzle = input[i+1]
	
	comsdict = dict()
	for itm in coms:
		comsdict[(itm[0],itm[1])] = itm[2]
		comsdict[(itm[1],itm[0])] = itm[2]
	
	elements = []
	
	for i in range(len(puzzle)):
		elements.append(puzzle[i])
		while len(elements) >= 2 and tuple(elements[-2:]) in comsdict:
			elements = elements[:-2] + [comsdict[tuple(elements[-2:])]]
		
		contains = set(elements)
		for opp in opps:
			if opp[0] in contains and opp[1] in contains:
				elements = []
				
	return elements
	

f = open(sys.argv[1])
out = open(sys.argv[1].replace("in","out"), "w")
cnt = int(f.readline().strip("\n"))
for i in range(cnt):
	input = f.readline().strip("\n").split(" ")
	
	output = solve(input)
	
	out.write("Case #%s: [%s]\n" % (i + 1, ", ".join(output)))
	print("Case #%s: [%s]\n" % (i + 1, ", ".join(output)))

