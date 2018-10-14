import sys,os

zaMatrix = [[ '1',  'i',  'j',  'k'],
	    [ 'i', '-1',  'k', '-j'],
            [ 'j', '-k', '-1',  'i'],
            [ 'k', 'j',  '-i', '-1'],
	   ]

zaElems = {'1':0,
	   'i':1,
	   'j':2,
           'k':3}

def readInput(filename):
	f = open(filename)
	lines = f.readlines()
	curentLine = 0
	nrTeste = int(lines[curentLine])
	for testu in range(nrTeste):
		curentLine +=1
		L,X = lines[curentLine].split()
		curentLine +=1
		L_char = lines[curentLine].strip()
		rezolva(testu, int(L), int(X), L_char)
	f.close()

def multiplyElements(elem1, elem2):
	ret = None

	if '-' in elem1 and '-' in elem2:
		ret = zaMatrix[ zaElems[elem1[1]] ][ zaElems[elem2[1]] ]
	
	if '-' in elem1 and '-' not in elem2:
		ret =  '-' + zaMatrix[ zaElems[elem1[1]] ][ zaElems[elem2] ]
	
	if '-' not in elem1 and '-' in elem2:
		ret = '-' + zaMatrix[ zaElems[elem1] ][ zaElems[elem2[1]] ]
	
	if ret is not None:
		ret = ret.replace('--', '')
	else:
		#print 'lol=', elem1, 'lol2=', elem2
		ret = zaMatrix[ zaElems[elem1] ][ zaElems[elem2] ]

	return ret


def prepare_IJK_string_old_version(L, X, L_char):
	# daca stringul 'compus' va avea mai putin de 8 caractere, il generam
	if L * X <= 8:
		return L_char*X, L*X

	if X > 8:
		X = X % 8

	return L_char*X, L*X

def prepare_IJK_string(L, X, L_char):
	return L_char*X, L*X

		
def doImultiplication(L_char):
	mul = '1'
	listForI = []
	for i in range(0, len(L_char), 1):
		mul = multiplyElements(mul, L_char[i])
		listForI.append(mul)
	return listForI

def doKmultiplication(L_char):
	mul = '1'
	listForK = []
	for i in range(len(L_char)-1, -1, -1):
		#print "[K] mul=%s" % mul,
		mul = multiplyElements(L_char[i], mul)
		#print " * %s = %s" % (L_char[i], mul)
		listForK.insert(0, mul)
	return listForK


def doMultiplication(L_char, start, stop):
	mul = '1'
	if start > stop:
		return None
	if start==stop:
		#print 'str=%s,%d' % (L_char, start)
		return L_char[start]
 
	#print "Fac MUL de la %s to %s" % (start,stop+1) 
	for i in range(start, stop+1):
		#print '\nDEBUG %s *`' % mul,
		mul = multiplyElements(mul, L_char[i])
		#print '%s = %s' % (L_char[i], mul)
	return mul
		
		
def rezolva(testu, L, X, L_char):
	ijk, size = prepare_IJK_string(L, X, L_char)
	#print "\nIJK=", ijk[:50]
	outText = "Case #%d: NO" % (testu+1)
	
	willContinue = doMultiplication(ijk, 0, len(ijk)-1) == '-1'

	if not willContinue:
		print outText
		return

	#print "From", L_char,"to", ijk[:50]
	#print "IJK", list(ijk)
	iList = doImultiplication(ijk)
	#print "I=",iList
        kList = doKmultiplication(ijk)
	#print "K=", kList

	for i in range(0, len(iList)-1, 1):
		if iList[i] == 'i':
			#print "Gasit I la pos", i
			for k in range(len(kList)-1, i, -1):
				#print "kList[%d] = %s" % (k, kList[k])
				if kList[k] == 'k':
					#print "Gasit K la pos", k
					res = doMultiplication(ijk, i+1, k-1)
					#print "J for IJK", list(ijk[i+1 : k])
					#print "multi for J", i+1, k-1, "res=", res
					if res == 'j':
						outText = "Case #%d: YES" % (testu+1)
						print outText
						return


	print outText
	return 
			
def test_multiplication():
	print '1*i=i', multiplyElements('1', 'i')
	print 'i*i=-1', multiplyElements('i', 'i')
	print 'k*i=j', multiplyElements('k', 'i')
	print 'j*i=-k', multiplyElements('j', 'i')
	print '-1*i=-i', multiplyElements('-1', 'i')
	print '-i*-j=k', multiplyElements('-i', '-j')
	print '-i*-j=k', multiplyElements('-i', '-j')
	print '-k*1=-k', multiplyElements('-k', '1')
	print '-k*j=i', multiplyElements('-k', 'j')

	print 'ijk=-1', doMultiplication('ijk', 0, 2)
	print 'jij=i', doMultiplication('jij', 0, 2)


	print 'ijk ijk ijk ijk ijk ijk ijk ijk ijk ijk = ?', doMultiplication('ijkijkijkijkijkijkijkijkijkijk', 0, 2)
	print 'ijk ijk ijk ijk ijk ijk ijk ijk ijk ijk = ?', doMultiplication('ijkijkijkijkijkijkijkijkijkijk', 0, 5)
	print 'ijk ijk ijk ijk ijk ijk ijk ijk ijk ijk = ?', doMultiplication('ijkijkijkijkijkijkijkijkijkijk', 0, 8)
	print 'ijk ijk ijk ijk ijk ijk ijk ijk ijk ijk = ?', doMultiplication('ijkijkijkijkijkijkijkijkijkijk', 0, 11)
	print 'ijk ijk ijk ijk ijk ijk ijk ijk ijk ijk = ?', doMultiplication('ijkijkijkijkijkijkijkijkijkijk', 0, 14)
	print 'ijk ijk ijk ijk ijk ijk ijk ijk ijk ijk = ?', doMultiplication('ijkijkijkijkijkijkijkijkijkijk', 0, 17)
	print 'ijk ijk ijk ijk ijk ijk ijk ijk ijk ijk = ?', doMultiplication('ijkijkijkijkijkijkijkijkijkijk', 0, 20)

	print 'ki ki ki ki ki = ?', doMultiplication('kikikikikiki', 0, 1)
	print 'ki ki ki ki ki = ?', doMultiplication('kikikikikiki', 0, 3)
	print 'ki ki ki ki ki = ?', doMultiplication('kikikikikiki', 0, 5)
	print 'ki ki ki ki ki = ?', doMultiplication('kikikikikiki', 0, 7)
	print 'ki ki ki ki ki = ?', doMultiplication('kikikikikiki', 0, 9)
	print 'ki ki ki ki ki = ?', doMultiplication('kikikikikikiki', 0, 11)
	print 'ki ki ki ki ki = ?', doMultiplication('kikikikikikiki', 0, 13)
	print 'ki ki ki ki ki = ?', doMultiplication('kikikikikikikiki', 0, 15)
	print 'ki ki ki ki ki = ?', doMultiplication('kikikikikikikikiki', 0, 17)
	print 'ki ki ki ki ki = ?', doMultiplication('kikikikikikikikikiki', 0, 19)
	print 'ki ki ki ki ki = ?', doMultiplication('kikikikikikikikikikiki', 0, 21)
	print 'ki ki ki ki ki = ?', doMultiplication('kikikikikikikikikikikiki', 0, 23)

	print 'ji ji ji ji ji .... = ?', doMultiplication('jijijijijijijijijijijijijijiji', 0, 27)
	print 'ji ji ji ji ji .... = ?', doMultiplication('jijijijijijijijijijijijijijiji', 0, 29)

if len(sys.argv)>1 and sys.argv[1]:
	inputFile = sys.argv[1]
else:
	inputFile = "test_input.txt"
#test_multiplication()
readInput(inputFile)                                      
	