fin = open("A-small-attempt1.in")
lines = fin.readlines()
fin.close()

fout = open("output.out", "w")
l = lines[1:]
caseNum = 1
count = 1
for line in l:
	line = line.strip('\n')
	temp = line[2:]
	#print temp
	total = 0
	toInvite = 0
	for i in range(len(temp)):
		if total < i:
			toInvite += (i - total)
			total = i + int(temp[i])
		else:
			#rint temp[i]
			total = int(temp[i]) + total
	s = 'Case #' + str(count) + ': ' + str(toInvite) + '\n'
	fout.write(s)
	count += 1
fout.close()