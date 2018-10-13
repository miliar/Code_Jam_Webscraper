#!/usr/bin/python

f = open('C-small-attempt0.in')
#f = open('c-input.in')
inputline = f.readline()
numcase = int(inputline)

#fout = open('rpi_small_result.txt', 'w')
fout = open('c_result.txt', 'w')


for i in range (0,numcase):
	line = f.readline()
	linelist = line.split()
	n = int(linelist[0])
	low = int(linelist[1])
	high = int(linelist[2])
	pfreq = []
	min_note = low
	possible = False

	line = f.readline()
	linelist = line.split()
	for j in range (0,n):
		pfreq.append(int(linelist[j]))

	for j in range (low,high+1):
		works = 0
		for k in range (0,n):
			rem = 0
			if j > pfreq[k]:
				rem = j % pfreq[k]
			elif pfreq[k] > j:
				rem = pfreq[k] % j
			else:
				rem = 0
			if rem!= 0:
				continue
			else:
				works = works + 1
		if works == n:
			possible = True
			min_note = j
			break
			

	if possible:
		answer = "Case #"+str(i+1)+": "+str(min_note)		
	else:
		answer = "Case #"+str(i+1)+": NO"
	print answer
	fout.write(answer)
	fout.write('\n')

