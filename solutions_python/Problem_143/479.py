import string

def get_rows(lines):
	if lines == 1:
		return map(int, raw_input().split())
	return [map(int, raw_input().split()) for _ in range(lines)]

def get_diff(a,b,k):
	total = 0
	for i in range(a):
		for j in range(b):
			if i&j < k:
				total += 1
	#print total
	return total

cases = input()
for i in range(1, cases + 1):
	a,b,k = get_rows(1)
	total = get_diff(a,b,k)
	print "Case #{0}: {1}".format(i, total)