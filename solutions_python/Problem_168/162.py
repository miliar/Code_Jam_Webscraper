arrows={'^':(-1,0),'>':(0,1),'v':(1,0),'<':(0,-1)}
T=int(input())
for t in range(T):
	R,C=map(int,input().split())
	rows=[input() for _ in range(R)]
	res=0
	valid=True
	for row in range(R):
		for col in range(C):
			if rows[row][col]=='.':
				continue
			diff=arrows[rows[row][col]]
			#check other row
			found=False

			other_row=row+diff[0]
			other_col=col+diff[1]
			while other_row>=0 and other_row<R and other_col>=0 and other_col<C:
				if rows[other_row][other_col]!='.':
					found=True
					break
				other_row=other_row+diff[0]
				other_col=other_col+diff[1]

			if found:
				continue

			#try others, not found
			for other_cell in arrows:
				other_diff=arrows[other_cell]
				if other_diff==diff:
					continue
				other_row=row+other_diff[0]
				other_col=col+other_diff[1]
				while other_row>=0 and other_row<R and other_col>=0 and other_col<C:
					if rows[other_row][other_col]!='.':
						found=True
						break
					other_row=other_row+other_diff[0]
					other_col=other_col+other_diff[1]
				if found:
					res+=1
					break
			if not found:
				valid=False
				break
		if not valid:
			break
	s="IMPOSSIBLE" if not valid else str(res)
	print("Case #%d: %s"%(t+1,s))

