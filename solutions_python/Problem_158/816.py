#encoding: utf-8

t = int(raw_input())

for case in range(t):
	x, r, c = [int(i) for i in raw_input().split()]
	winner = 'RICHARD'

	if x == 1:
		winner = 'GABRIEL'
	elif x == 2:
		if (r*c)%2 == 0:
			winner = 'GABRIEL'
	elif x == 3:
		if r>1 and c>1 and (r==3 or c==3):
			winner = 'GABRIEL'
	elif x == 4:
		if r*c==16 or r*c == 12:
			winner = 'GABRIEL'

	print 'Case #'+str(case+1)+': '+winner
