#!/usr/bin/python

def sort(s):
	l = [c for c in s]
	l.sort()
	res = ""
	for i in l:
		res += i
	return res

t = int(raw_input())

for g in xrange(t):
	n = raw_input()
	found = False

	for i in range(len(n)-1, 0, -1):
		a = n[i-1]
		b = n[i]
		if (a < b):
			k = len(n)-1
			for j in n[:(i-1):-1]:
				if (j > a): break
				k -= 1
			if (k < 0): raise Error('BUM')
			n = n[:(i-1)] + n[k] + sort(n[(i-1):k] + n[(k+1):])
			found = True
			break

	if (not found):
		n = '0' + n[::-1]
		k = 0
		for j in n:
			if (j != '0'): break
			k += 1
		
		n = n[k] + n[:k] + n[(k+1):]

	print "Case #" + str(g+1) + ": " + str(int(n))
