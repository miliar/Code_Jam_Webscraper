def testcasehandler():
	#gets 10 lines of data, turn into a list 
	case = []
	for x in range(10): 
		line = f.next().strip('\n')
		v = line.split(" ")
		for u in v:
			u = int(u)
			case.append(u)
	return case

def findcard(cnum, case):
	a1 = case[0]
	a2 = case[17]

	row1 = case[a1*4-3:a1*4+1]
	row2 = case[a2*4+17-3:a2*4+17+1]

	print row1, row2, set(row1).intersection( set(row2))

	if len( set(row1).intersection( set(row2) ) ) == 1: 
		print "Case #"+str(cnum)+":", set(row1).intersection( set(row2)).pop()
	elif len( set(row1).intersection( set(row2) ) ) > 1: 
		print "Case #"+str(cnum)+": Bad magician!"
	elif len( set(row1).intersection( set(row2) )) == 0:
		print "Case #"+str(cnum)+": Volunteer cheated!"
	else:
		print "ERROR"

if __name__ == "__main__":
	f = open('/Users/stefsy/code/codejam2014/magicinput.txt','r')
	# first line = number of cases 
	cases = int(f.readline())
	bigholder = [] 
	for n in range(1,cases+1):
		bigholder.append(testcasehandler())
	f.close() 

	for x in range(0,len(bigholder)):
		findcard(x+1, bigholder[x])

