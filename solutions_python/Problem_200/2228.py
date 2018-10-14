
'''
def check_tidy(n):
	digitn = str(n)
	c = 0
	for d in digitn:
		if c < int(d):
			c = int(d)
		elif c > int(d):
			return False
	return True
'''

def generate_9s(n):
	a = ""
	for i in range(n):
		a = a+"9"
	return a

def find_tidy(n):
	str_n = str(n)
	i = len(str_n)-2
	while i >= 0:
		if int(str_n[i]) > int(str_n[i+1]):
			str_n = str_n[:i] + str(int(str_n[i])-1) + generate_9s(len(str_n)-1-i)
		i = i-1
	return int(str_n)


# Std I/O Module
t = int(input())
for i in range(1, t + 1):
	n = int(input())
	print("Case #%d: %d" %(i, find_tidy(n)))