a = open("my.in2")
def tho(myint):
	if (myint < 10):
		return "000"+str(myint)
	elif (myint>=10 and myint < 100):
		return "00"+str(myint)
	elif (myint >=100 and myint< 1000):
		return "0"+ str(myint)
	else:
		return str(myint)
def fever(str):
	a= {}
	for k in xrange(19):
		a[k] = 0
	for t in xrange(len(str)-1,-1,-1):
		if str[t] == 'm':
			a[18] = (a[18] + 1)
			a[5] = (a[5] + a[6])
		if str[t] == 'a':
			a[17] = a[17] + a[18]
		if str[t] == 'j':
			a[16] = a[16] + a[17]
		if str[t] == ' ':
			a[15] = a[15] + a[16]
			a[10] = a[10] + a[11]
			a[7] = a[7] + a[8]
		if str[t] == 'e':
			a[14] = a[14] + a[15]
			a[6] = a[6] + a[7]
			a[1] = a[1] +a[2]
		if str[t] == 'd':
			a[13] = a[13] + a[14]
		if str[t] == 'o':
			a[12] = a[12] + a[13]
			a[4] = a[4] + a[5]
			a[9] =a[9]+a[10]
		if str[t] == 'c':
			a[11] = a[11] + a[12]
			a[3] = a[3] + a[4]
		if str[t] == 't':
			a[8] = a[8] + a[9]
		if str[t] == 'l':
			a[2] = a[2] + a[3]
		if str[t] == 'w':
			a[0] = a[0] + a[1]
	return a[0]%10000
t = int(a.readline())
for k in xrange(t):
	print "Case #"+str(k+1)+":",tho(fever(a.readline()))
