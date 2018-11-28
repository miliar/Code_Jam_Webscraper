f = open('A-small-attempt1.in')
out = open('ABF.out','w')
i = 0
for line in f:
	if i==0:
		i = i + 1
		continue
	n = int(line)
	out.write('Case #' + str(i) + ': ' + str(NToNumber[n]) + '\n')
	i = i + 1

out.close()

