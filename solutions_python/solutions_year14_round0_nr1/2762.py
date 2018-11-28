
inputfile = "A-small-attempt0.in"
outfile = inputfile.split(".")[0]+".out"
# print outfile
fin = open(inputfile,'r')
fout = open(outfile,'w')
testcases = int(fin.readline())
# print testcases

for casenum in range(1,testcases+1):
	# print casenum
	row1 = int(fin.readline())
	matrix1 = [map(int,fin.readline().strip().split()) for i in range(4)]
	# print row1,'\n',matrix1

	row2 = int(fin.readline())
	matrix2 = [map(int,fin.readline().strip().split()) for i in range(4)]
	# print row2,'\n',matrix2

	cards1 = set(matrix1[row1-1])
	cards2 = set(matrix2[row2-1])
	# print cards1,cards2

	intersect = cards1.intersection(cards2)
	# print intersect,len(intersect)

	if len(intersect)==1:
		# print ('Case #%d: %d\n'%(casenum,intersect.pop()))
		fout.write('Case #%d: %d\n'%(casenum,intersect.pop()))
	elif len(intersect) == 0:
		fout.write("Case #%d: Volunteer cheated!\n"%casenum)
	else:
		fout.write("Case #%d: Bad magician!\n"%casenum)





