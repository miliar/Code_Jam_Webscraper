def count_friends(smax, peeps):
	standing = 0
	friends = 0
	for j in range(len(peeps)):
		p = int(peeps[j])
		while standing < j:
			friends += 1
			standing += 1
		standing += p
	return friends

inputt = open('ovin.txt','r')
outfile = open('output.txt', 'w')
totals = inputt.readline()

i = 1
for line in inputt:
	(smax, peeps) = line.split()
	outputt = count_friends(smax, peeps)
	outfile.write('Case #%s: %s\n' %(i, outputt))
	i += 1
