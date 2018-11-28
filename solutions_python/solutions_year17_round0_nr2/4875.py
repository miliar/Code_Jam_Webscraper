def tidyNumbers4(N):
	Nstr = str(N)
	Nint = int(N)
#	print len(Nstr)
#	print Nint

	found = False

	sortedNstr = ''.join(sorted(Nstr))
	if Nstr == sortedNstr:
		return Nstr

	numList = []
	for char in Nstr:
		numList.append(int(char))
#	print numList

	for i in range(len(numList)-1):
		if numList[i] >= numList[i+1]:
#			print i
#			print numList[i+1:]
			for j in range(i+1,len(numList)):
				numList[j] = 9
			break
#	print numList
#	print i

	numList[i] += -1

	for k in range(i-1,0,-1):
		if numList[k] > numList[k+1]:
			numList[k] += -1

#	print numList

	output = ''
	for l in range(len(numList)):
		if l == 0 and numList[l] == 0:
			continue
		output = output + str(numList[l])
#	print output
	return output

from itertools import islice

infile = open("Tidy_Numbers_small.txt", 'r')
outfile = open("Tidy_numbers_small_output.txt", 'w')
size = infile.readline()
size = int(size)
countline = 0

for line in islice(infile, 0, size+1):
	countline += 1
	linestring = str(countline)
	output = tidyNumbers4(int(line))
	output = str(output)

	outfile.write("Case #" + linestring + ": " + output)
	outfile.write('\n')

infile.close()
outfile.close()
