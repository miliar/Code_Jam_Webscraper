#!/usr/bin/python

f = open("C-small-attempt0.in", "r")

T = int(f.readline())

def palindrome(num):
	strNum = str(num)
	l = len(strNum)

	for i in range(l/2):
		if strNum[i] != strNum[l-i-1]:
			return False

	return True

for t in range(1, T+1):

	lb, ub = map(int, f.readline().strip().split())

	c = 0
	for i in range(lb, ub+1):
		if palindrome(i):
			root = int(i**0.5)
			if root*root == i and palindrome(root):
				c += 1

	print "Case #{0}: {1}".format(t, c)

