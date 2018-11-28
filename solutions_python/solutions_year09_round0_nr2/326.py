import pprint

T=int(raw_input())

def f(B, (x,y)):
	for n,t in enumerate(B):
		if (x,y) in t:
			return n
			
for case_no in range(T):
	m=[]
	H,W=map(int, raw_input().strip().split(' '))
	
	for j in range(H):
		m.append(map(int, raw_input().strip().split(' ')))
	
	B=[]
	M=[]
	for i in range(H):
		r=[]
		for j in range(W):
			B.append([(i,j)])
			t=[]
			n=10**100
			for y,x in [(i-1,j), (i,j-1), (i,j+1), (i+1,j)]:
				try:
					d=m[y][x]
					if x>=0 and y>=0:
						t.append((y,x))
						n=d if d<n else n
				except: pass
			
			if n<m[i][j]:
				Y,X=i,j
				for y,x in t:
					if m[y][x]==n:
						Y,X=y,x
						break
				
				r.append((Y,X))
			else:
				r.append((i,j))
				
		M.append(r)

	for i in range(H):
		for j in range(W):
			t=True if (i,j)==M[i][j] else False
			m=f(B, (i,j))
			n=f(B, M[i][j])
			s1=set(B[m])
			s2=set(B[n])
			B[m]=[]
			if not t: B[n]=[]
			n=min((m,n))
			B[n].extend(s1 | s2)
	
	for i in range(len(B)-1, -1, -1):
		if not B[i]: del B[i]
	
	
	
	d={}
	for i in range(len(B)):
		for j in B[i]:
			d[j]=i
	
	print "Case #%d:" % (case_no+1)
	
	x=[]
	s=''
	for i in range(H):
		for j in range(W):
			t=d[(i,j)]
			if t not in x: x.append(t)
			print chr(97+x.index(t)),
		print
