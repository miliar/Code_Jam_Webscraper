def nToLst(n):
	ret = []
	while n:
		ret.append(n % 10)
		n /= 10
	return ret[::-1]

def lstToN(lst):
	x = lst[0] if len(lst) else 0
	for i in xrange(1, len(lst)):
		x = x * 10 + lst[i]
	return x

def calc2(n):
	lst = nToLst(n)
	temp, minVal = [], float('inf')
	for i in xrange(len(lst)-1, -1, -1):
		minVal = min(minVal, lst[i])
		temp = [minVal] + temp

	replace = False
	i = 0
	while i < len(temp):
		if replace:
			temp[i] = 9
		elif lst[i] > temp[i]:
			while i < len(lst) and lst[i + 1] >= lst[i]:
				temp[i] = lst[i]
				i += 1
			temp[i] = lst[i] - 1
			replace = True

		i += 1


	return lstToN(temp)

def calc(n):
	lst = nToLst(n)
	i = 0
	while i < len(lst) - 1 and lst[i] <= lst[i+1]:
		i += 1
	if i != len(lst) - 1:
		while i > 0 and lst[i] == lst[i-1]:
			i -= 1
		lst[i] -= 1
		for j in xrange(i + 1, len(lst)):
			lst[j] = 9
	return lstToN(lst)



t = input()
for i in xrange(t):
	n = input()
	print "Case #%d:" % (i + 1), calc(n)
	#print n, "->", calc(n)