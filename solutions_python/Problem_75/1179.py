import os, sys, math

infile = open(sys.argv[1], "r")

T = int(infile.readline())

def stringtolist(string):
	if len(string) == 0:
		return "[]"
	ret = "["
	for s in string[:-1]:
		ret = ret + s + ", "
	ret = ret + string[-1] + "]"
	return ret

for x in range(0, T):
	line = infile.readline().split()
	
	combine = {}
	temp = line[1:int(line[0])+1]
	for t in temp:
		combine[t[:2]] = t[2]
	start = int(line[0])+2
	end = int(line[0])+2+int(line[int(line[0])+1])
	
	oppose = line[start:end]
	magicks = line[int(line[0])+2+int(line[int(line[0])+1])+1]
	queue = ""
	for m in magicks:
		queue = queue + m
		if len(queue) >= 2:
			key = queue[-2:]
			if combine.has_key(key):
				rep = combine[key]
				queue = queue[:-2]
				queue = queue + rep
				for opp in oppose:
					if rep in opp and opp.replace(rep, "") in queue:
						queue = ""
			elif combine.has_key(key[::-1]):
				
				rep = combine[key[::-1]]
				queue = queue[:-2]
				queue = queue + rep
				for opp in oppose:
					if rep in opp and opp.replace(rep, "") in queue:
						queue = ""
			else:
				for opp in oppose:
					if m in opp and opp.replace(m, "") in queue:
						queue = ""
		
	print "Case #%d: %s" % (x+1, stringtolist(queue))