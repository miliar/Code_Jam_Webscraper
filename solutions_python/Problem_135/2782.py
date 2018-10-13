T = int(raw_input())
f = open('A-small-out.txt', 'w')
for t in xrange(1, T + 1):
	ra = int(raw_input())
	a = []
	a.append( raw_input().split(' ') )
	a.append( raw_input().split(' ') )
	a.append( raw_input().split(' ') )
	a.append( raw_input().split(' ') )
	
	rb = int(raw_input())
	b = []
	b.append( raw_input().split(' ') )
	b.append( raw_input().split(' ') )
	b.append( raw_input().split(' ') )
	b.append( raw_input().split(' ') )
	
	s = [ x for x in a[ra - 1] if x in b[rb - 1] ]
	if len(s) == 1:
		ans = str(s[0])
	elif len(s) > 1:
		ans = 'Bad magician!'
	else:
		ans = 'Volunteer cheated!'
	r = 'Case #%d: %s' % (t, ans)
	f.write(r+'\n')

