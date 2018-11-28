import itertools
def myprint(a):
	s = ""
	for i in a:
		s = s + str(i) + " "
	
	s = s.strip()
	s = s + "\n"
	
	return s
	
def go(fileLine):
	subsets = {}
	for setLength in range(1, 21):
		subset = itertools.combinations(map(int, fileLine), setLength)
		subsetdict = {}
		for i in subset:
			if(sum(i) in subsets):
				if(subsets[sum(i)] == i):
					continue
				output.write(myprint(i) + myprint(subsets[sum(i)]))
				return
			subsetdict[sum(i)] = i
		subsets = dict(subsets.items() + subsetdict.items())		
			
output = open('outputC.txt', 'w')
counter = 0
with open('inputC.txt', 'r') as f:
	for fileLine in f:
		fileLine = fileLine.split()
		if (counter == 0):
			counter = counter + 1
			continue
		n = float(fileLine.pop(0))
		output.write("Case #" + str(counter) + ":")
		output.write("\n")
		go(fileLine)	
		
		counter = counter + 1

output.close()
f.close()
