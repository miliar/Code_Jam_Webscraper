nc = input()

for i in range(1,nc+1):
	number = list(raw_input())
	output = ""
	
	for j in range(len(number)-1, 0, -1):
		cur = int(number[j])
		prev = int(number[j-1])
		if cur >= prev:
			continue
		else:
			number[j-1] = str(prev - 1)
			for q in xrange(j,len(number)):
				number[q] = str(9)

	if number[0] == '0':
		number=number[1:]

	output = ''.join(number)
	print "Case #%d: %s"%(i, output)
