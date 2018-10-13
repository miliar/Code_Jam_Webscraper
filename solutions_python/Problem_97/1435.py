import sys

A = 0
B = 0

def has_same_digits(n,m):
	return len(str(n)) == len(str(m))

def generate_recycles(n):
	ret = []
	str_n = str(n)
	for i in range(1, len(str_n)):
		str_m = str_n[i:] + str_n[:i]
		str_m.replace('0','')
		m = int(str_m)
		if (n < m <= B) and has_same_digits(n,m) and not (m in ret):
			ret.append(m)
	return ret

input = open(".\C-small-attempt0.in", "r")
num_of_cases = int(input.readline())
for i in range(1,num_of_cases+1):
	result = 0
	A, B = input.readline().split()
	A = int(A)
	B = int(B)
	for j in range(A,B+1):
		result = result + len(generate_recycles(j))
	print "Case #%d: %d" % (i, result)
