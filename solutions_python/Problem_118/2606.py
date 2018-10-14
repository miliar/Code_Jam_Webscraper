'''Google Code Jam 2013'''
'''Qualification Round'''
'''C. Fair and Square'''
'''@author ationsong@gmail.com'''

import math

def isPalindrome(inStr):
	l = len(inStr)

	i = 0
	while i < l/2:
		if not inStr[i] == inStr[l - i - 1]:
			return False
		i = i+1

	return True

def processFile(name):
	f = open(name, 'r')
	lines = f.readlines()

	T = int(lines[0].split(' ')[0].strip())
	#print "Cases:" + str(T)

	i = 1
	while (i <= T):

		L = lines[i].split(' ')
		A = int(L[0].strip())
		B = int(L[1].strip())

		#print "From " + str(A) + " to " + str(B)

		j = int(math.ceil(math.sqrt(A)))
		bound = int(math.floor(math.sqrt(B)))
		count = 0

		while (j <= bound):
			if isPalindrome(str(j)) and isPalindrome(str(int(math.pow(j, 2)))):
				#print str(j) + " " + str(int(math.pow(j, 2)))
				count += 1

			j += 1

		print "Case #" + str(i) + ": " + str(count)

		i += 1

processFile('C-small-attempt0.in')