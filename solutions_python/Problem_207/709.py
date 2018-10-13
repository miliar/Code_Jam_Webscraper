# Train Script

from collections import defaultdict as dd
from heapq import heapify, heappop, heappush

T=input()
for zz in range(T):
	N, R, O, Y, G, B, V = [int(i) for i in raw_input().split(' ')]
	if O>B or G>R or V>Y: 
		print 'Case #%d: %s'%(zz+1, 'IMPOSSIBLE')
		continue
	if B!=0 and B==O:
		if R+G+Y+V==0: print 'Case #%d: %s'%(zz+1, 'BO'*B)
		else: print 'Case #%d: %s'%(zz+1, 'IMPOSSIBLE')
		continue
	if R!=0 and R==G:
		if B+O+Y+V==0: print 'Case #%d: %s'%(zz+1, 'RG'*R)
		else: print 'Case #%d: %s'%(zz+1, 'IMPOSSIBLE')
		continue
	if Y!=0 and Y==V:
		if R+G+B+O==0: print 'Case #%d: %s'%(zz+1, 'YV'*Y)
		else: print 'Case #%d: %s'%(zz+1, 'IMPOSSIBLE')
		continue
	B,R,Y=B-O,R-G,Y-V
	z=[(B,'B'),(R,'R'),(Y,'Y')]
	z.sort(lambda a,b: cmp(b[0],a[0]))
	if z[0][0]>z[1][0]+z[2][0]:
		print 'Case #%d: %s'%(zz+1, 'IMPOSSIBLE')
		continue
	vb=['B']+['OB' for i in range(O)]
	vr=['R']+['GR' for i in range(G)]
	vy=['Y']+['VY' for i in range(V)]
	
	ans=[]
	m1,m2,m3=z[0][0],z[1][0],z[2][0]
	k=m2+m3-m1
	for i in range(m1):
		if m2>0: 
			ans.append(z[0][1])
			if k>0: 
				ans.append(z[2][1])
				k-=1
			ans.append(z[1][1])
			m2-=1
		elif m3>0:
			ans.append(z[0][1])
			ans.append(z[2][1])
			m3-=1
	l1,l2,l3=-1,-1,-1
	if 'B' in ans: l1=ans.index('B')
	if 'R' in ans: l2=ans.index('R')
	if 'Y' in ans: l3=ans.index('Y')
	if l1!=-1: ans[l1]=''.join(vb)
	if l2!=-1: ans[l2]=''.join(vr)
	if l3!=-1: ans[l3]=''.join(vy)
	print 'Case #%d: %s'%(zz+1,''.join(ans))
	