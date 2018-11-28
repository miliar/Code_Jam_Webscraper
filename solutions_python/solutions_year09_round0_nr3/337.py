S="welcome to code jam"
L=len(S)

N=int(raw_input())

def ch(s, c, i):
	global S
	x=[]
	while True:
		try:
			i=s.index(S[c], i)
			x.append(i)
			i+=1
		except: break
	return x

def f(s, c=0, i=[]):
	global S, L, count
	
	if c==0 and i!=[0]:
		f(s, 0, [0])
		return

	if c==L+1:
		count+=1
		return
	
	for j in i:
		x=ch(s, c, j)
		f(s, c+1, x)
		
for i in range(N):
	s=raw_input().strip()
	
	count=0
	f(s)
	print "Case #%d: %04d" % (i+1, count%10000)
	
