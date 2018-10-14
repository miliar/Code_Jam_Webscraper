import sys

def readData():
	fn = sys.argv[1]
	fh = open(fn)
	foh = open(fn.replace("in", "out"), "w")
	ncases = int(fh.readline())
	for case in range(ncases):
		foh.write("Case #%i: %s\n" % (case + 1, standOvation(fh.readline())))
	fh.close()
	foh.close()

def standOvation(caseLine):
	case = caseLine.split()
	shyest = case[0]
	audience = case[1]
	friends = 0
	stand = 0
	
	for i, person in enumerate(audience):
		if stand >= shyest:
			break
		elif stand < i:			
			friends += 1
			stand += 1 
			if stand == i: stand += int(person)
		else:
			stand += int(person)
	
	return str(friends)				

readData()
