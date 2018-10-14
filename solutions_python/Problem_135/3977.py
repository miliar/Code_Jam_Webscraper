import os, sys

lines = tuple(open(sys.argv[1], 'r'))


testCasesCount = int(lines[0])

linesI = 1
while testCasesCount > 0:

	guess1 = lines[linesI].rstrip()
	guess1Rows = [lines[linesI+1].rstrip(),lines[linesI+2].rstrip(),lines[linesI+3].rstrip(),lines[linesI+4].rstrip()]
	guess2 = lines[linesI+5].rstrip()
	guess2Rows = [lines[linesI+6].rstrip(),lines[linesI+7].rstrip(),lines[linesI+8].rstrip(),lines[linesI+9].rstrip()]
	
	testCasesCount -= 1
	row1 = guess1Rows[int(guess1)-1].rsplit(" ")
	row2 = guess2Rows[int(guess2)-1].rsplit(" ")
	result = list(set(row1).intersection(row2))
	case = str(linesI/10 + 1)
	if len(result) == 1:
	 print "Case #"+case+": "+result[0]
	elif len(result) > 1:
	 print "Case #"+case+": Bad magician!"
	elif len(result) == 0:
	 print "Case #"+case+": Volunteer cheated!"
	linesI += 10

