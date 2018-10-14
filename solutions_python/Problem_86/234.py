testName = 'C'
testName = 'C-small-attempt0'
#testName = 'B-large'
#testName = 'B-test'

inputFile = open(testName+'.in', 'r')
input = inputFile.read()
inputFile.close()
del inputFile

output = ""

lines = input.split("\n")
pop = lines.pop
del input

T = int( pop(0) )

for t in range(T):
	(N, L, H) = map(int, pop(0).split())
	freqs = map(int, pop(0).split())

	n = L
	while n <= H:
		found = True
		for i in freqs:
			if i % n > 0 and n % i > 0:
				found = False
				break
		if found: break
		n += 1
	print n
	#print y - (y % 0.000001)
	if found:
		output += "Case #%d: %d\n" % (t+1, n)
	else:
		output += "Case #%d: NO\n" % (t+1)

print output

outputFile = open(testName+'.out', 'w')
outputFile.write(output)
outputFile.close()
