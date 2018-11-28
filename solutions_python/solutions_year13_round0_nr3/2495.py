import sys

def fair(i):
	x = str(i)
	if '.0' in x:
		x = x[:-2]
	elif '.' in x:
		return False
	x = list(x)
	return (x == x[::-1])
	
def square(i):
	root = i ** 0.5
	return fair(root)

fil = open('testd.txt')

for case in range(int(fil.readline())):
	a, b = fil.readline().split()
	a, b = int(a), int(b)
	nums = 0
	for i in range(a, b + 1):
		if fair(i) and square(i):
			nums += 1
	print "Case #{}: {}".format(case + 1, nums)