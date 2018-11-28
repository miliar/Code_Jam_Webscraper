def isTidy(n):
	t = True
	s = str(n)
	if len(s) == 1:
		t = True	
	last =  s[0]
	for x in s[1:]:
		#print last, x
		if int(last) > int(x):
			t = False
			break
		last = x
	return t


for t in range(input()):
	n = input()
	res = False
	if isTidy(n) == True:
		res = True
	else:
		while n >= 0:
			n -= 1
			res = isTidy(n)
			if res == True:
				break
	print "case #{}: {}".format(t+1, n)
