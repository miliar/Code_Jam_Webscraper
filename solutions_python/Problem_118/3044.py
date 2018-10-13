# Google Code Jam 2013 Qualification Round Question 3 - Fair and Square

## import deel van numpy iewers
import numpy as np
#import scipy as sp

from numpy import loadtxt


#---- GET INPUT -------------------------------------------------
inp = open('input.txt','r')
out = open('output.txt','w')

numbercases = inp.readline()
numbercases = int(numbercases)

cases = np.loadtxt('input.txt', skiprows=1)

#cases = inp.readlines()
print 'number of cases: %d' %(numbercases)
print 'cases imported'


#---- TEST PALINDROME ---------------------------------------------
def palindrometest(number):
	reverse = 0
	temp = number
	while(temp >= 1):
		reverse = reverse * 10
		reverse = reverse + int(temp%10)
		#reverse = reverse + (temp%10-temp%1)
		temp = temp/10
	return (number==reverse)


#---- Investigate a Case -------------------------
def docase(low,high):
	fairsquares = 0
	
	low = np.sqrt(low)
	if (low%1>0):
		low +=1
	low = int(low)
	high = int(np.sqrt(high))
	
	for i in range(low,high+1):
		if (palindrometest(i)):
			if (palindrometest(i**2)):
				fairsquares += 1
				print i**2
	
	return fairsquares

	
#---- CALCULATIONS ------------------------------------------------

fq_number=0 #number of fairsquares found

for i in range(numbercases):
	fq_number = docase(cases[i,0],cases[i,1])
	outstring = "Case #%d: %d\n" % (i+1,fq_number)
	out.write(outstring)
	# CALCS HIER
	

#---- OUTPUT  ------------------------------------------------------------
#---- END ------------------------------------------------------------

inp.close()
out.close()



