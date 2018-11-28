#!/usr/bin/env python
import sys

f = open(sys.argv[1]).readlines()
count = 0
data = []
totalCases = f[0]
f.pop(0)

while f != []:
	a,b = f[0].split()
	d = [int(a), int(b)]
	data.append(d)
	f.pop(0)

case = 1
#Code starts here
f = open(sys.argv[1]+".out", "w")

def isPalindrome(num):
	reversedNum = int(str(num)[::-1])
	if num == reversedNum:
		return True
	else:
		return False

def isPerfectSquare(x):
	ans = 0
	while ans*ans < x:
		ans += 1
		if ans*ans == x:
			return ans
	return 0


for d in data:
	count = 0
	print "==================="
	print d
	start, finish = d
	for num in range(start,finish+1):
		#print num
		# First, find out if num is a palindrome...
		if isPalindrome(num) == True:
			#print num
			# Then find out if it is a perfect square
			ans = isPerfectSquare(num)
			if ans > 0:
				# Finally, find if root is also a perfect square
				if isPalindrome(ans) == True:
					print num
					count += 1
	lineOut = "Case #"+str(case)+": "+str(count)
	print lineOut
	f.write(lineOut+"\n")
	case += 1
f.close()
