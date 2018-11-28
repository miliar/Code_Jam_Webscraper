def checkStand(audience):
	standing = 0
	for i in range(0,len(audience)):

		if standing >= i:
			standing += audience[i]
		else:
			return False

	# Everyone stood
	return True

filename_in = 'A-large.in'
filename_out = 'aud-A-large.out'

fin = open(filename_in,'r')
fout = open(filename_out,'w')

print(int(fin.readline()))
casenum = 0

for l in fin:
	casenum += 1
	ls = l.split()
	print('people: ' + str(int(ls[0])))
	aud = []
	for x in range(0,int(ls[0])+1):
		aud.append(int(ls[1][x]))
	
	add =  0
	while not checkStand(aud):
		add += 1
		aud[0] += 1

	fout.write('Case #' + str(casenum) + ': ' + str(add) +'\n')

fin.close()
fout.close()