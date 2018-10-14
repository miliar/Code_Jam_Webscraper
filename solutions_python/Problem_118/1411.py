#!/usr/bin/python

import sys, math, gmpy

palindromes = {}

def isPalindrome(phrase):

    phrase_letters = [c for c in phrase.lower()]
    #print phrase_letters  # test
    return (phrase_letters == phrase_letters[::-1])

def check(num):
	'''
		if num is palindrome then add to palindrome dict
		if it is a perfect square then, check if square root is palindrome

	'''
	if isPalindrome(str(num)):
		'''
		'''

		if gmpy.is_square(num):
			sq_root = int(math.sqrt(num))
			if isPalindrome(str(sq_root)):
				return True



	return False




if len(sys.argv) != 2:
    print "Please run program: python file.py inputFilename"
    sys.exit()

try:
    f = open(sys.argv[1],'r')
    count = int(f.readline())
except IOError:
    print "Input File could not be opened"
    sys.exit()

case = 1

while count > 0:#{
	
	line = f.readline()
	if not line:
		f.close()
		break

	line.rstrip()
	(A, B) = line.split(' ')
	A = int(A)
	B = int(B)

	cnt = 0

	while A <= B:
		if check(A):
			cnt = cnt + 1

		A = A + 1

	print "Case #" + str(case) + ": " + str(cnt)

	case = case + 1
	count = count - 1

