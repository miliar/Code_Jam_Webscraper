import sys,math





def multiply(a,b):
	multiplymap = {
		'1':{'1':'1','i':'i','j':'j','k':'k'},
		'i':{'1':'i','i':'-1','j':'k','k':'-j'},
		'j':{'1':'j','i':'-k','j':'-1','k':'i'},
		'k':{'1':'k','i':'j','j':'-i','k':'-1'}
	}

	asign = 1
	bsign = 1
	if a[0] == '-': 
		asign = -1
		a = a[1:]
	if b[0] == '-': 
		bsign = -1
		b = b[1:]
	resultsign = asign*bsign
	if resultsign == 1:
		minus = ''
	else:
		minus = '-'

	result = multiplymap[a][b]

	if minus == '-':
		if result[0] == '-':
			result =result[1:]
		else:
			result = '-' + result

	return result





def solveString(s):
	s = list(s)

	first = '1'

	for i in range(len(s)):

		first = multiply(first,s[0])

		s = s[1:]

	return first

def prepreliminaryChecks(s,times):
	if len(set(s)) == 1:
		return False


	a = solveString(s)
	
	if a == '1':
		return False
	if a == '-1' and times % 2 == 0:
		return False
	if a == 'i' and times % 4 != 2:
		return False
	if a == 'j' and times % 4 != 2:
		return False
	if a == 'k' and times % 4 != 2:
		return False
	if a == '-i' and times % 4 != 2:
		return False
	if a == '-j' and times % 4 != 2:
		return False
	if a == '-k' and times % 4 != 2:
		return False





	return True

def preliminaryChecks(s):
	if len(s) < 3:
		return False

	return True

def solveProblem(s):

	if preliminaryChecks(s) == False:
		#sys.stderr.write("preliminarychecks failed.\n");
		return False

	#print "here"

	for i1 in range(1,len(s)-1):
		#print i1

		if len(s) - i1 > i1: #fastest condition
			cond1 = solveString(s[0:i1]) == 'i'
		else:
			cond1 = solveString(s[i1:]) == 'i'

		if cond1:
			for i2 in range(i1+1,len(s)):
				#print "i1: " + str(i1) + "i2: " + str(i2)
				if len(s)-i2 > i2-i1: #the easiest condition
					cond2 = (solveString(s[i1:i2]) == 'j')
				else:
					cond2 = (solveString(s[i2:]) == 'k')
				if cond2:
					#print "woooo"
					return True

	return False



#s = raw_input()
cases = int(raw_input())
rows = []

for i in range(cases):
	num = raw_input().split(' ')
	length = int(num[0])
	times = int(num[1])
	string = raw_input()

	#print "processing " + string

	if prepreliminaryChecks(string,times):
		if solveProblem(string*times):
			result = 'YES'
		else:
			result = 'NO'
	else:
		#print "prepre!"
		result = 'NO'
	
	print ("Case #" + str(i+1) + ": " + result)


