#f = file("A-small-attempt0.in")
f = file("A-large.in")
#f = file("test.in")
#of = file("A-small-attempt0.out", "w")
of = file("A-large.out", "w")
#of = file("test.out", "w")

def calc(p, k, l, letterFreq):
	letterFreq.sort()
	letterFreq.reverse()
	print letterFreq
	result = 0
	presses = 1
	keyIndex = 0
	for i in range(l):
		result += letterFreq[i] * presses
		
		keyIndex += 1
		if keyIndex >= k:
			keyIndex = 0
			presses += 1
			
	return result

cases = int(f.readline().strip())
for case in range(cases):
	print "Processing case", case + 1
	v = f.readline().strip().split()
	p = int(v[0])
	k = int(v[1])
	l = int(v[2])

	letterFreq = []	
	v = f.readline().strip().split()
	for letter in v:
		letterFreq.append(int(letter))

	result = calc(p, k, l, letterFreq)
	print "Result:", result
	
	of.write("Case #" + str(case + 1) + ": ")
	of.write(str(result))		
	of.write("\n");