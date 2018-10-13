def make_tidy(ar):
	i = len(ar)
	if i == 1:
		return ar
	i-=1
	
	while i > 0:
		if ar[i-1] > ar[i]:
			for ii in range(i, len(ar)):	
				ar[ii] = 9
			ar[i-1] -= 1
		elif ar[i] <= 0:
			ar[i] = 9
			ar[i-1] -=1
		i-=1

	if ar[0] <= 0:
		return ar[1:]
	return ar

def tidy(i):
	last = str(i)[0]
	for c in str(i)[1:]:
		if int(last) > int(c):
			return False
		last = c
	return True

t = input()
for tc in range(t):
	n = input()
	while True:
		if tidy(n):
			break
		else:
			ar = make_tidy([int(x) for x in str(n)])
			n = 0
			for i in ar:
				n *= 10
				n += i
	print "Case #{0}: {1}".format(tc +1, n)