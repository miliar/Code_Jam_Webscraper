import sys, os
from string import rstrip, split

# Open files to read and write
fin = open(os.getcwd() + '/' + sys.argv[1], 'r')
fout = open(os.getcwd() + '/' + sys.argv[1] + '.out', 'w')

# Process the input
numCases = int(rstrip(fin.readline(), '\n'))

for case in xrange(numCases):
	k = int(rstrip(fin.readline(), '\n'))
	rest = split(rstrip(fin.readline(), '\n'), ' ')[1:]
	perfect = []
	perfect.append(k)
	lastIndex = 0
	
	krange = xrange(k-1, 0, -1)
	for cur in krange:
		steps = (cur+1) % len(perfect)
		nextIndex = lastIndex - steps + 1 # might be MINUS ONE instead of PLUS ONE!!!!
		if (nextIndex < 0):
			nextIndex += len(perfect)
		perfect.insert(nextIndex, cur)
		lastIndex = nextIndex
		
	# shift that shit
	newPerf = []
	for i in xrange(len(perfect)):
		newPerf.append(0)
	
	for i in xrange(len(perfect)):
		newElem = i + lastIndex
		if (newElem >= len(perfect)):
			newElem -= len(perfect)
		newPerf[i] = perfect[newElem]
	output = "Case #%d:" % (case + 1)
	for index in rest:
		output += (" %d" % newPerf[int(index)-1])
	output += "\n"
	
	fout.write(output)


# Close the input file stream
fin.close()
# Close the output file stream
fout.close()
