def isPalindrome(num):
	st = str(num)
	for i in range(len(st) / 2):
		if(st[i] != st[-(i + 1)]):
			return False
	return True

def prepare():
	for i in range(1, 10**7 + 1):
		if(isPalindrome(i) and isPalindrome(i**2)):
			all.append(int(i**2))

def find(x):
	l = 0
	r = len(all)
	x = int(x)
	while(l < r):
		m = (l + r) / 2
		if(all[m] <= x and x < all[m + 1]):
			print m
			return m
		elif(all[m] < x):
			l = m + 1
		else:
			r = m
	return -1 

def count(x, y):
	x = int(x)
	y = int(y)
	c = 0
	i = 0
	while(all[i] < x):
		i += 1
	while(i < len(all) and all[i] <= y):
		c += 1
		i += 1
	return c

def readFromFile():
	ins = open("data.txt", "r")
	for line in ins:
		all.append(int(line))	
		
T = input()
all=[]
prepare()
#readFromFile()
#print all

for i in range(T):
	line = raw_input()
	a, b = int(line.split(" ")[0]), int(line.split(" ")[1])
	print "Case #" + str(i + 1) + ": " + str(count(a, b))

