import pprint

def read_file(file):
	f = open(file,'r')
	count = 0
	cases = []
	for line in f:
		count += 1
		if count == 1:
			t = int(line.strip())
		elif count % 2 == 0:
			n = int(line.strip())
		else:
			temp = line.strip().split()
			case = []
			for x in temp:
				case.append(int(x))
			cases.append(case)
	return cases
			
def Denary2Binary(n):
# convert denary integer n to binary string bStr
# from http://www.daniweb.com/software-development/python/code/216539

	bStr = ''
	if n < 0: raise ValueError, "must be a positive integer"
	if n == 0: return '0'
	while n > 0:
		bStr = str(n % 2) + bStr
		n = n >> 1
	return bStr
	
def AddWrong(bina,binb):
	iter = 1
	if len(bina) >= iter:
		amore = True
	else: amore = False
	if len(binb) >= iter:
		bmore = True
	else: bmore = False
	string = ''
	while amore == True or bmore == True:
		if amore == True: a = int(bina[-iter])
		else: a = 0
		if bmore == True: b = int(binb[-iter])
		else: b = 0
		c = a + b
		if c == 2:
			c = 0
		string = str(c) + string
		iter += 1
		if len(bina) >= iter:
			amore = True
		else: amore = False
		if len(binb) >= iter:
			bmore = True
		else: bmore = False
	return string
	
def SumSeries(series):
	maxval = 0
	binSumA = {'':'0'}
	binSumB = {'':'0'}
	regSumA = {'':0}
	regSumB = {'':0}
	for index,item in enumerate(series):
		print index
		binTempA = {}
		binTempB = {}
		regTempA = {}
		regTempB = {}
		for k in binSumA:
			string = k + 'A'
			binTempA[string] = AddWrong(binSumA[k],Denary2Binary(item))
			binTempB[string] = binSumB[k]
			regTempA[string] = regSumA[k] + item
			regTempB[string] = regSumB[k]
			string = k + 'B'
			binTempA[string] = binSumA[k]
			binTempB[string] = AddWrong(binSumB[k],Denary2Binary(item))
			regTempA[string] = regSumA[k]
			regTempB[string] = regSumB[k] + item
		binSumA = binTempA
		binSumB = binTempB
		regSumA = regTempA
		regSumB = regTempB
	#print pp.pprint(binSumA)
	#print pp.pprint(binSumB)
	#print pp.pprint(regSumA)
	#print pp.pprint(regSumB)
	for k in binSumA:
		if int(binSumA[k],2) == int(binSumB[k],2):
			if min([regSumA[k],regSumB[k]]) > 0:
				val = max([regSumA[k],regSumB[k]])
				if val > maxval:
					maxval = val
	return maxval
	
pp = pprint.PrettyPrinter(indent=4)

#print int(AddWrong(Denary2Binary(12),Denary2Binary(5)),2)
#print int(AddWrong(Denary2Binary(5),Denary2Binary(4)),2)
#print int(AddWrong(Denary2Binary(7),Denary2Binary(9)),2)
#print int(AddWrong(Denary2Binary(5),Denary2Binary(6)),2)

cases = read_file('C-small-attempt4.in')
#print pp.pprint(cases)

for index,case in enumerate(cases):
	val = SumSeries(case)
	if val == 0:
		output = "Case #%d: NO" % (index+1)
	else:
		output = "Case #%d: %d" % (index+1,val)
	f = open('candy.out','a')
	print >>f, output
	f.close()



			