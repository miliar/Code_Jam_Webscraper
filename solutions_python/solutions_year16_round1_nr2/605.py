def solve(l):
	backup = list(l)
	d = []
	j = 0 
	laux = []
	ans = [i for i in range(len(l[0]))]
	for i in range(len(l[0])):
		l.sort(key = lambda a: a[i])
		if len(l) == 1 or l[0][i] != l[1][i]:
			j = i
			laux = l[0]
			break
		l.pop(0)
		l.pop(0)
	l = backup
	for i in range(len(l[0])):
		l.sort(key = lambda a: a[i])
		
		if i != j:
			l1 = l[0]
			l2 = l[1]
			if laux[i] == l1[j]:
				ans[i] = l2[j]
			else:
				ans[i] = l1[j]
			l.pop(0)
		else:
			ans[i] = laux[j]
		l.pop(0)

	
	return " ".join(map(str,ans))







f = open("B-large (1).in")
T = int(f.readline())
for case in range(1,T+1):
	r = int(f.readline())
	l = []
	for i in range(r*2-1):
		l.append(map(int,f.readline().split(" ")))
	print "Case #{0}: ".format(case) + solve(l)
