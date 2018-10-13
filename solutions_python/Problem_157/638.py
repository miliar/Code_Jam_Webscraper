def prod(a,b):
	if a=='1':
		return b
	elif a=='-1':
		return '-'+b
	elif a=='i':
		if b=='i':
			return '-1'
		elif b=='j':
			return 'k'
		elif b=='k':
			return '-j'
	elif a=='j':
		if b=='i':
			return '-k'
		elif b=='j':
			return '-1'
		elif b=='k':
			return 'i'
	elif a=='k':
		if b=='i':
			return 'j'
		elif b=='j':
			return '-i'
		elif b=='k':
			return '-1'
	elif a=='-i':
		if b=='i':
			return '1'
		elif b=='j':
			return '-k'
		elif b=='k':
			return 'j'
	elif a=='-j':
		if b=='i':
			return 'k'
		elif b=='j':
			return '1'
		elif b=='k':
			return '-i'
	elif a=='-k':
		if b=='i':
			return '-j'
		elif b=='j':
			return 'i'
		elif b=='k':
			return '1'

T=int(raw_input())
for n in range(T):
	line=raw_input().split()
	reps=int(line[1])
	size=int(line[0])
	word=raw_input()
	sequence=''
	for m in range(reps):
		sequence+=word
	pos=0
	firstProd='1'
	while firstProd!='i' and pos<reps*size:
		firstProd=prod(firstProd,sequence[pos])
		pos+=1
	secondProd='1'
	while secondProd!='j' and pos<reps*size:
		secondProd=prod(secondProd,sequence[pos])
		pos+=1
	thirdProd='1'
	while pos<reps*size:
		thirdProd=prod(thirdProd,sequence[pos])
		pos+=1
	if firstProd=='i' and secondProd=='j' and thirdProd=='k':
		print 'Case #'+str(n+1)+': YES'
	else:
		print 'Case #'+str(n+1)+': NO'
