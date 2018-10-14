f = open('A-small-attempt3.in')
T = int(f.__next__()[:])
x = 1
while x<=T:
	k = f.__next__()

	Snum = k[2:]
	Si = 0
	Slist = list(Snum)
	Slist.pop()
	Speople=0
	m = 0
	while m < len(Slist):
		if Slist[m] == '0' and Si < m+1:
			Si+=1
			Speople+=1
			m+=1
		elif Slist[m] != '0' or not Si < m+1:
			Si += int(Slist[m])
			m+=1
		elif m == len(Slist):
			break
	g = open('text.txt', 'a')
	g.write('Case #%d: %s\n' % (x, Speople))
	x+=1