#!/usr/bin/python
def getLine(lineNum, fobj):
	print("line num is %d" %lineNum)
	for j in range (1, 5) :
		print("reading line %d" %j)
		if (j == lineNum) :
			row1 = fobj.readline().rstrip('\n')
		else:
			dummy = fobj.readline()
	return row1
	
def main() :
	fobj = open("magic-input")
	writeobj = open("output1.txt", 'w')
	caseNum = int(fobj.readline())
	print("No of cases is %d" %caseNum)
	i = 0
	for i in range (0, caseNum) :
		firstAns = int(fobj.readline())
		list1 = getLine(firstAns, fobj).split(' ')

		secondAns = int(fobj.readline())
		list2 = getLine(secondAns, fobj).split(' ')
		count = 0
		ix = 0
		for l in list1 :
			if l in list2 :
				count= count+1
				ix = int(l)
		if count > 1:
			writeobj.write("Case #%d: Bad magician!\n" %(i+1))
		elif count == 0:
			writeobj.write("Case #%d: Volunteer cheated!\n" %(i+1))
		else :
			writeobj.write("Case #%d: %d\n" %(i+1, ix))

	writeobj.close()
	fobj.close()

main()
