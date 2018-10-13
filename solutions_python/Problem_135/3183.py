T = input()
fOut = open('codejam1.out','w')
for case in xrange(T):
	row1 = input()
	grid1 = list()
	for i in range(4):
		grid1.append(map(int,raw_input().split()))

	row2 = input()
	grid2 = list()
	for i in range(4):
		grid2.append(map(int,raw_input().split()))

	nums = set(grid2[row2-1]).intersection(set(grid1[row1-1]))
	fOut.write("Case #" + str((case+1)) + ': ');
	if(len(nums) > 1):
		fOut.write('Bad magician!\n');
	elif(len(nums) == 0):
		fOut.write('Volunteer cheated!\n');
	else:
		fOut.write(str(list(nums)[0]));
		fOut.write('\n')
fOut.close()