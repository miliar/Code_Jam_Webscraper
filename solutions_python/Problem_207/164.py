fo = open('big.txt','w')
with open('test.txt') as f:
	lines = f.readlines()
	lines = [_.strip() for _ in lines]
	for i,line in enumerate(lines[1:]):
		es = [int(_) for _ in line.split()]
		n = es[0]
		r,o,y,g,b,v = es[1:]
		try:

			assert (g<r) or (g==r and g+r==n) or (g==0)
			assert (o<b) or (o==b and o+b==n) or (o==0)
			assert (v<y) or (v==y and v+y==n) or (v==0)
			if v==y and v>0:
				res='YV'*y
			elif o==b and o>0:
				res='OB'*o
			elif g==r and g>0:
				res='GR'*g
			else:
				r-=g
				b-=o
				y-=v
				arr = [('R',r),('B',b),('Y',y)]
				arr = sorted(arr,key=lambda x: x[1])
				assert arr[0][1]+arr[1][1]>=arr[2][1]
				two = (arr[0][0]+arr[1][0])*arr[0][1]+arr[1][0]*(arr[1][1]-arr[0][1])
				res=[]
				k = len(two)-1
				for _ in range(arr[2][1]):
					res+=[arr[2][0],two[k]]
					k-=1
				if k>=0:
					res+=two[:k+1][::-1]
				res = ''.join(res)
				# print res
				res = res.replace('R','RG'*g+'R',1)
				res = res.replace('B','BO'*o+'B',1)
				res = res.replace('Y','YV'*v+'Y',1)

			fo.write('Case #{}: {}\n'.format(i+1, res))
		except:
			fo.write('Case #{}: {}\n'.format(i+1, 'IMPOSSIBLE'))

fo.close()
