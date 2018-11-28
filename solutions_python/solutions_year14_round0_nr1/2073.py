f = open('crom.txt','r')

t = int(f.readline())

for x in range(t):
	l1 = int(f.readline())
	for x1 in range(1,5):
		lines = f.readline()
		if x1 == l1:
			lines = lines.replace('\n','')
			fl = lines.split(' ')

	l2 = int(f.readline())
	for x2 in range(1,5):
		lines = f.readline()
		if x2 == l2:
			lines = lines.replace('\n','')
			sl = lines.split(' ')

	ans = [y for y in fl if y in sl] #+ [y for y in sl if y not in fl]

	if len(ans) == 1:
		print 'Case #' + str(x+1) + ': ' + str(ans[0])
	elif len(ans) > 1:
		print 'Case #' + str(x+1) + ': Bad magician!'
	else:
		print 'Case #' + str(x+1) + ': Volunteer cheated!'