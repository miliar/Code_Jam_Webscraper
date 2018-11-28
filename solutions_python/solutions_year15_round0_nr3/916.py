infile = open('file.in','r')
outfile = open('out.txt','w')
t = int(infile.readline())
oneD = {'1':'1','i': 'i','j': 'j','k': 'k'}
iD =   {'1':'i','i':'-1','j': 'k','k':'-j'}
jD =   {'1':'j','i':'-k','j':'-1','k': 'i'}
kD =   {'1':'k','i': 'j','j':'-i','k':'-1'}
firstD = {'1':oneD,'i':iD,'j':jD,'k':kD}
def multiply(val1,val2):
	val1=str(val1)
	val2=str(val2)
	#print val1, val2
	if len(val1)==1:
		return firstD[val1][val2]
	else:
		newVal = '-' + firstD[val1[1]][val2]
		if len(newVal)==3:
			return newVal[2]
		else:
			return newVal
def findResult(string,x):
	string = string*x
	val = string[0]
	iIndexes = []
	for count in range(0,len(string)-1):
		if val=='i':
			iIndexes.append(count)
		val = multiply(val,string[count+1])
	if len(iIndexes) == 0:
		return False
	else:
		for start in iIndexes:
			jStrings = string[start+1:]
			jVal = jStrings[0]
			jIndexes = []
			for jcount in range(0,len(jStrings)-1):
				if jVal=='j':
					jIndexes.append(jcount)
				jVal = multiply(jVal,jStrings[jcount+1])
			if len(jIndexes) == 0:
				break
			for kStart in jIndexes:
				kStrings = jStrings[kStart+1:]
				kVal = kStrings[0]
				for kCnt in range(1,len(kStrings)):
					kVal = multiply(kVal,kStrings[kCnt])
				if kVal =='k':
					return True
			return False
for i in range(t):
	line = infile.readline().split()
	l = int(line[0])
	x = int(line[1])
	string = infile.readline()[:-1]
	cnt = 0
	iVal = False
	jVal = False
	kVal = False
	for v in string:
		if v == 'i' and not iVal:
			cnt +=1
			iVal = True
		elif v=='j' and not jVal:
			cnt+=1
			jVal = True
		elif not kVal:
			cnt+=1
			kVal = True
	if cnt < 2 or len(string)*x<3:
		result = False
	else:
		result = findResult(string,x)
		if result == True:
			print "yep"
		else:
			print "nope"
	if result==True:
		outfile.write("Case #"+str(i+1)+": YES\n")
	else:
		outfile.write("Case #"+str(i+1)+": NO\n")
	

