from sys import stdin

def isPalindrome(x):
	return str(x) == ''.join(reversed(str(x)))

def genPalindrome(bound):
	ans = []
	for i in range(1,10):
		ans.append(i)
	for i in range(1,10):
		ans.append(int(str(i) + str(i)))
	i = 1
	lastdigit = 1
	digit = 1
	while(1):
		if digit != lastdigit:
			lasti = i
			for x in range(pow(10, digit) - lasti):
				cons = 0
				rev = ''.join(reversed(str(i)))
				n = int(str(i) + rev)
				if n <= bound:
					cons = 1
					ans.append(n)
				i += 1
				if cons == 0:
					break
			lastdigit = digit
			i = lasti
		rev = ''.join(reversed(str(i)))
		cons = 0
		for x in range(10):
			n = int(str(i) + str(x) + rev)
			if n <= bound:
				cons = 1
				ans.append(n)
		i += 1
		digit = int(len(str(i)))
		if cons == 0:
			break
	return ans

def genSquarePalindrome(pal_list, bound):
	ans = []
	for p in pal_list:
		p2 = pow(p,2)
		if p2 <= bound and isPalindrome(p2):
			ans.append(p2)
	return ans

pals = genPalindrome(pow(10,8))
squarePals = genSquarePalindrome(pals, pow(10,15))

T = int(stdin.readline())
for t in range(T):
	A, B = [int(x) for x in stdin.readline().strip().split()]
	count = 0
	for a in squarePals:
		if A <= a <= B:
			count += 1
	print("Case #%d: %d" % (t+1, count))