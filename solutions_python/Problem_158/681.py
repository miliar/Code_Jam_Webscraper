casesRichard={
	'1x1':['2','3','4'],
	'1x2':['3','4'],
	'2x1':['3','4'],
	'1x3':['2','3','4'],
	'3x1':['2','3','4'],
	'1x4':['3','4'],
	'4x1':['3','4'],
	'2x2':['3','4'],
	'2x3':['4'],
	'3x2':['4'],
	'2x4':['3','4'],
	'4x2':['3','4'],
	'3x3':['2','4'],
	'3x4':[],
	'4x3':[],
	'4x4':['3']
}
T=int(raw_input())
t=T
while t:
	x,r,c=map(int,raw_input().split())
	castr=str(r)+'x'+str(c)
	tmp=casesRichard[castr]
	try:
		tmp.remove(str(x))
		print 'Case #'+str(T-t+1)+': RICHARD'
	except:
		print 'Case #'+str(T-t+1)+': GABRIEL'
	t-=1
