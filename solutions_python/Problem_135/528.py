fin=open("A-small-attempt0.in","r")
fout=open("output.txt","w")

def getRow(rowNumber):
	row = []

	for rowI in xrange(4):
		tmp = fin.readline()
		if rowI == (rowNumber - 1):
			row = tmp
	return row

cases=int(fin.readline())

for case in xrange(cases):
	row1Number = int(fin.readline())
	row1 = getRow(row1Number).rstrip().split(" ")

	row2Number = int(fin.readline())
	row2 = getRow(row2Number).rstrip().split(" ")
	
	duplicates = [c for c in row1 if c in row2]
	
	if len(duplicates) == 1:
		result = str(duplicates[0]) 
	elif len(duplicates) == 0:
		result = "Volunteer cheated!" 
	else: 
		result = "Bad magician!"

	fout.write("Case #{0}: {1}\n".format(str(case + 1) , result))
fin.close()
fout.close()

