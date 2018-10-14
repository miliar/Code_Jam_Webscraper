
import numpy as np

def generatenumbers(xifres,minV,maxV):
	np = 0;
	for a in range(1,10):
		if xifres == 1:
			nombre = int(str(a))
			if checknum(nombre,minV,maxV):
				np += 1
		elif xifres == 2:
			nombre = int(str(a) + str(a))
			if checknum(nombre,minV,maxV):
				np += 1
		else:
			for b in range(0,10):
				if xifres == 3:
					nombre = int(str(a) + str(b) + str(a))
					if checknum(nombre,minV,maxV):
						np += 1
				elif xifres == 4:
					nombre =  int(str(a) + str(b) + str(b) + str(a))
					if checknum(nombre,minV,maxV):
						np += 1
				else:
					for c in range(0,10):
						if xifres == 5:
							nombre = int(str(a) + str(b) + str(c) + str(b) + str(a))
							if checknum(nombre,minV,maxV):
								np += 1
						elif xifres == 6:
							nombre = int(str(a) + str(b) + str(c) + str(c) + str(b) + str(a))
							if checknum(nombre,minV,maxV):
								np += 1
						else:
							for d in range(0,10):
								if xifres == 7:
									nombre = int(str(a) + str(b) + str(c) + str(d) + str(c) + str(b) + str(a))
									if checknum(nombre,minV,maxV):
										np += 1
								elif xifres == 8:
									nombre = int(str(a) + str(b) + str(c) + str(d) + str(d) + str(c) + str(b) + str(a))
									if checknum(nombre,minV,maxV):
										np += 1
	return np							

def checknum(nombre,minV,maxV):
	if (nombre >= minV) and (nombre <= maxV):
		#print nombre
		return isPalindrome(nombre*nombre)
	else:
		return False

def isPalindrome(a):
	b = str(a)
	palindrome = True
	for i in range (0,len(b)/2):
		if b[i] != b[-i-1]:
			palindrome = False
			break
	return palindrome


def readInput(filename):
	fid = open(filename, 'r')
	T = int(fid.readline())
	R = []
	for zzz in range(0,T):
		#print '****************'
		print str(zzz)
		line = fid.readline().rstrip('\n').split()
		#print line	
		
		minV = int(line[0])	
		maxV = int(line[1])	
		minsq = int(np.ceil(np.sqrt(minV)))
		maxsq = int(np.floor(np.sqrt(maxV)))
	
		nP = 0
		
		minDigits = len(str(minsq))
		maxDigits = len(str(maxsq))
		
		#print "Values: " + str(minV) + "-" + str(maxV)
		#print "Squares" + str(minsq) + "-" + str(maxsq)
		#print "Digits" + str(minDigits) + "-" + str(maxDigits)
		
		for digits in range(minDigits,maxDigits+1):
			nP += generatenumbers(digits,minsq,maxsq)

		#print nP
		#when solution is obtained do 
		R.append(nP)
	
	print R
	fileOut = filename[0:-2] + 'out'
	writeSolution(R,fileOut)




def writeSolution(R,filename):
	idx = 1
	fid = open(filename,'w')
	for line in R:
		h = 'Case #' + str(idx) + ': ' 
		hh = h + ''.join(str(line)) + '\n'
		fid.write(hh)
		idx += 1
	fid.close()




#D=readInput('sample')
#D=readInput('C-small-attempt0.in')
D=readInput('C-large-1.in')


