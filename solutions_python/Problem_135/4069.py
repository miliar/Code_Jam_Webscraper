f_in = open('A-small-attempt2.in', 'r')
f_out = open('A-small-attempt2.out', 'w')

cases = f_in.readline()

outputs = []

for i in range(int(cases)):

	rowA = []
	rowB = []

	for a in range(5):
		rowA.append(f_in.readline().replace('\n', ''))

	for b in range(5):
		rowB.append(f_in.readline().replace('\n', ''))

	rowAA = rowA[int(rowA[0])].split(' ')
	rowBB = rowB[int(rowB[0])].split(' ')

	matches = []

	for aa in range(4):
		for bb in range(4):

			if(rowAA[aa] == rowBB[bb]):
				matches.append(rowAA[aa])

	if(len(matches) == 1):
		out = 'Case #%i: %s' % (i+1, matches[0])
	elif(len(matches) == 0):
		out = 'Case #%i: Volunteer cheated!' % (i+1)
	else:
		out = 'Case #%i: Bad magician!' % (i+1)

	outputs.append(out)


f_out.write('\n'.join(outputs))
f_out.close()