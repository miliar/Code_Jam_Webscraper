def consec(conv, n):
	for i in range(len(conv) - n + 1):
		count = 0
		for j in range(n):
			count += conv[i + j]
		if count == n:
			return True
	return False

f = open('A-small-attempt0.in.txt','r')
g = open('output.txt', 'w')

T = int(f.readline())

for z in range(T):
	coun = 0
	nam, n = f.readline().strip().split()
	n = int(n)
	conv = []
	for i in nam:
		if i in ["a","e","i","o","u"]:
			conv.append(0)
		else:
			conv.append(1)
	for i in range(len(conv) - n + 1):
		j = 0
		echeck = 0
		hold = i
		namcheck = conv[i:]
		while consec(namcheck,n) == True and echeck == 0:
			coun += 1
			j = len(namcheck) - 1
			if len(namcheck) == n:
				echeck = 1
			else:
				namcheck = namcheck[:j]
	g.write('Case #%d: %d\n' % (z+1,coun))
	