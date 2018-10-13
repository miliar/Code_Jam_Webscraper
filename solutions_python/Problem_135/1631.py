outwr = ''
mgf = open('magic.txt', 'r')
conts = mgf.read().split('\n')
mgf.close()

cases = int(conts[0])
sinO = 1
sinT = 6
for cn in range(cases):
	arO = [int(i) for i in conts[sinO + int(conts[sinO])].split(' ')]
	arT = [int(i) for i in conts[sinT + int(conts[sinT])].split(' ')]
	print (arO, arT)
	badM = False
	badV = True
	same = -1
	for i in arO:
		for j in arT:
			if i==j:
				if same != -1: badM = True
				badV = False
				same = i
	if badV: out = 'Volunteer cheated!'
	elif badM: out = 'Bad magician!'
	else: out = str(same)
	sinO += 10
	sinT += 10
	outwr += 'Case #' + str(cn+1) + ': ' + out + '\n'

outf = open('out.txt', 'w')
outf.write(outwr)
outf.close()