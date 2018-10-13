#!/usr/bin/python

def pernesti():
	dat = None
	with open("input.txt", 'rb') as ff:
		dat = ff.read()

	if dat == None or len(dat) < 1:
		print "File read failed.."
		return -1

	data = dat.split("\r\n")
	#print "LEN DATA: ",len(data)-1		
	testcases = data[0]
	#print data
	#print "Testcases: ",testcases,"\n"

	if len(data) < 11 and testcases > 0:
		print "invalid data"
		return -1
		
	if (len(data)-2)%10 != 0:
		print "missing data"
		return -1

	res = []
	for i in range(1, len(data), 10):
		#print i
		if data[i] == "":
			continue
		first = int(data[i])
		second = int(data[i+5])
		rows_f = data[i+1:i+5]
		rows_s = data[i+6:i+10]
		
		#print "First row guess: ",first,"\n",'\n'.join([x for x in rows_f]),"\nSecond row guess: ",second,"\n",'\n'.join([x for x in rows_s])

		fguess = rows_f[first-1]
		sguess = rows_s[second-1]
		#print "\nguess in\n",fguess,"\n",sguess,"\n"

		ff=fguess.split(" ")
		#print "FF: ",ff
		ff=[int(d) for d in ff]
		#print ff
		
		ss=sguess.split(" ")
		ss = [int(d) for d in ss]
		valid = []
		for x in range(0,4):
			if ff[x] in ss and ff[x] != " ":
				valid.append(ff[x])
		if len(valid) == 1:
			res.append(valid[0])
		if len(valid) > 1:
			res.append("Bad magician!")
		if len(valid) == 0:
			res.append("Volunteer cheated!")

	for i in range(0, int(testcases)):
		print "Case #%i: %s" % (i+1,res[i])
	return 0

pernesti()