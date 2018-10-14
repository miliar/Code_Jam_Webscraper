from codejam import *
for uu in range(rt(int)):
	n, A, B, C, D, x0, y0, M = rl(int)
	
	X = x0
	Y = y0
	
	ff=[[0,0,0],[0,0,0],[0,0,0]]
	
	tree=[]
	tree.append((X,Y))
	ff[X%3][Y%3]+=1
	for i in range(1, n):
		X = (A * X + B) % M
		Y = (C * Y + D) % M
		tree.append((X,Y))
		ff[X%3][Y%3]+=1
		
	
	#print ff

	ans=0
	for x1 in range(3):
		for x2 in range(3):
			for x3 in range(3):
				for y1 in range(3):
					for y2 in range(3):
						for y3 in range(3):
							if (x1+x2+x3)%3==0 and (y1+y2+y3)%3==0:
								if (x1,y1)==(x2,y2)==(x3,y3):
									if ff[x1][y1]>=3:
										ans+=(ff[x1][y1]-0)*(ff[x2][y2]-1)*(ff[x3][y3]-2)
								elif (x1,y1)==(x2,y2):
									if ff[x1][y1]>=2:
										ans+=(ff[x1][y1]-0)*(ff[x2][y2]-1)*(ff[x3][y3]-0)
								elif (x1,y1)==(x3,y3):
									if ff[x1][y1]>=2:
										ans+=(ff[x1][y1]-0)*(ff[x2][y2]-0)*(ff[x3][y3]-1)
								elif (x2,y2)==(x3,y3):
									if ff[x1][y1]>=2:
										ans+=(ff[x1][y1]-0)*(ff[x2][y2]-0)*(ff[x3][y3]-1)
								else:
									ans+=ff[x1][y1]*ff[x2][y2]*ff[x3][y3]
				
	hd()				
	print ans/6
	
	continue
				

	count=0
	for i in range(n):
		for j in range(i+1,n):
			for k in range(j+1,n):
				if (tree[i][0]+tree[j][0]+tree[k][0]) % 3 == 0 and (tree[i][1]+tree[j][1]+tree[k][1]) % 3 == 0:
#					print tree[i],tree[j],tree[k]
					count+=1
	hd()
	print count
				

