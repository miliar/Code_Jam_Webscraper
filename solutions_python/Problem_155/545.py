f = open('test.txt', 'r')

f.readline()
caseN=1
for line in f:
	need = 0;
	sofar = 0;
	maxP = int(line[0])
	l=line.split()[1].strip()
	counts=[int(a) for a in l]
	for i in range(0,len(counts)):
		count = counts[i]
		#print count, sofar, need, i
		if sofar >= i:
			sofar += count
			continue
		else:
			need += i - sofar
			sofar += count + i - sofar
			continue
	print "Case #%d: %d" % (caseN, need)
	caseN += 1

		


