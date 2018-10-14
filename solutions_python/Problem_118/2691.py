import math

def ispalindrome(number):
	return str(number) == str(number[::-1])

def ispalindrome5(x):  
	z = str(x)  
	if len(z)==1:
		return True
	l=len(z)/2  
	if z[:l]==z[-l:][::-1]:  
		return True  
	return False

def isPerfectSquare(root):
	if int(root) == root:
		return True
	return False 

#open file
f = open('./C-small-attempt0.in', 'r')

#count input puzzle
numberOfLines = f.readline()

for k in range(int(numberOfLines)):
	line=f.readline()
	nums = [int(n) for n in line.split()]
	min = nums[0]
	max = nums[1]

	count=0
	for i in range(min,max+1):
		root = math.sqrt(i)
		if isPerfectSquare(root):
			root=int(root)
			if ispalindrome5(root):
				if ispalindrome5(i):
					count=count+1
	print 'Case #'+ str(k+1) + ': ' + str(count)
