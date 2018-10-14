from math import *
inputName = "inputc"
outputName = "outputc"
f = open(inputName, "r")
out = open(outputName , "w")

def isPalindrome(num):
	n = num
 	rev = 0
 	while n > 0:
		dig = n % 10
		rev = rev * 10 + dig
		n = n / 10

	if num == rev:
		return True
	return False

def is_square(apositiveint):
	if apositiveint == 1:
		return True
	x = apositiveint // 2
	seen = set([x])
	while x * x != apositiveint:
		x = (x + (apositiveint // x)) // 2
		if x in seen: return False
		seen.add(x)
	return True
 


def average(a, b):
	return (a + b) / 2.0
def improve(guess, x):
	return average(guess, x/guess)
def good_enough(guess, x):
	d = abs(guess*guess - x)
	return (d < 0.001)
def square_root(guess, x):
	while(not good_enough(guess, x)):
		guess = improve(guess, x)
	return guess
def new_sqrt(x):
	r = int(square_root(1, x))
	return r

def calculate(a,b):
	counter = 0
	for x in range(a,b+1):
		#print x , "isPalindrome ",isPalindrome(x), "is_square ",is_square(x),"square_root ",new_sqrt(x) 
		if isPalindrome(x) and is_square(x) and isPalindrome(new_sqrt(x)):
			counter += 1
	return counter

def solve():
	t = int(f.readline())
	for i in range(1,t+1):
		#print i
		line = f.readline().split(" ")
		a = int(line[0])
		b = int(line[1])
		#print "Case #"+str(i)+":",calculate(a,b)
		print >> out , "Case #"+str(i)+":",calculate(a,b)
	f.close()
	out.close()

solve()