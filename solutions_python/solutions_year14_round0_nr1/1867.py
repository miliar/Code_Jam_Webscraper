def cnt(a,b):
	t=0
	for i in a:
		if i in b:
			t+=1
	return t
def getcommon(a,b):
	for i in a:
		if i in b:
			return i
for case in xrange(input()):
	print 'Case #'+`(case+1)`+":",
	a1,a=input(),[]
	for i in [0]*4:
		a.append(list(x for x in raw_input().split(' ')))
	b1,b=input(),[]
	for i in [0]*4:
		b.append(list(x for x in raw_input().split(' ')))
	ans=cnt(a[a1-1],b[b1-1])
	if ans==1:
		print getcommon(a[a1-1],b[b1-1])
	elif ans==0:
		print 'Volunteer cheated!'
	else:
		print 'Bad magician!'
	