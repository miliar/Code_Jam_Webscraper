def mult(curr, n):
	if curr == '1':
		return n
	if curr == '-1':
		return ("-" + n)
	if curr == 'i':
		if n == '1':
			return "i"
		if n == 'i':
			return "-1"
		if n == 'j':
			return "k"
		if n == 'k':
			return "-j"
	if curr == 'j':
		if n == '1':
			return "j"
		if n == 'i':
			return "-k"
		if n == 'j':
			return "-1"
		if n == 'k':
			return "i"
	if curr == 'k':
		if n == '1':
			return 'k'
		if n == 'i':
			return 'j'
		if n == 'j':
			return "-i"
		if n == 'k':
			return "-1"
	if curr == '-i':
		if n == '1':
			return "-i"
		if n == 'i':
			return "1"
		if n == 'j':
			return "-k"
		if n == 'k':
			return "j"
	if curr == '-j':
		if n == '1':
			return "-j"
		if n == 'i':
			return "k"
		if n == 'j':
			return "1"
		if n == 'k':
			return "-i"
	if curr == '-k':
		if n == '1':
			return '-k'
		if n == 'i':
			return '-j'
		if n == 'j':
			return "i"
		if n == 'k':
			return "1"	

for p in xrange(input()):
	l, x = map(int, raw_input().split())
	st = raw_input()
	st = st * x
	l *= x
	curr = '1'
	for i in xrange(l):
		curr = mult(curr, st[i])
		if curr == 'i':
			break
	if i+1 == l:
		print "Case #"+str(p+1)+": NO"
		continue
	curr = '1'
	for j in xrange(i+1, l):
		curr = mult(curr, st[j])
		if curr == 'j':
			break
	if j+1 == l:
		print "Case #"+str(p+1)+": NO"
		continue				
	curr = '1'
	for k in xrange(j+1, l):
		curr = mult(curr, st[k])
	if curr == 'k':
		print "Case #"+str(p+1)+": YES"
	else:
		print "Case #"+str(p+1)+": NO"