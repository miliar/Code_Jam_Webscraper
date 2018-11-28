def solve(info):
	(r,c)=map(int,info.split(" "))
	cake=[]
	for z in range(0,r):
		cake.append(list(raw_input()))
	rect=[]
	for row in range(0,r):
		for col in range(0,c):
			if cake[row][col]!='?':
				rect.append([cake[row][col],row,col,row,col])
	return '\n'+pr(expand(rect,r,c),cake)
def expand(rects,_r,c):
	if intereset(rects):
		return False
	if win(rects,_r,c):
		return rects
	for r in range(0,len(rects)):
		r=rects[r]
		if r[1]>0:
			r[1]=r[1]-1
			res=expand(rects,_r,c)
			if res !=False:
				return res
			r[1]=r[1]+1
		if r[2]>0:
			r[2]=r[2]-1
			res=expand(rects,_r,c)
			if res !=False:
				return res
			r[2]=r[2]+1
		if r[3]<_r-1:
			r[3]=r[3]+1
			res=expand(rects,_r,c)
			if res !=False:
				return res
			r[3]=r[3]-1
		if r[4]<c-1:
			r[4]=r[4]+1
			res=expand(rects,_r,c)
			if res !=False:
				return res
			r[4]=r[4]-1
	return False
def win(rects,_r,c):
	sum =0
	for r in rects:
		sum=sum+(r[3]-r[1]+1)*(r[4]-r[2]+1)
	return sum==_r*c
def intereset(rects):
	for r1 in rects:
		for r2 in rects:
			if r1==r2:
				continue
			h_overlaps = (r1[1] <= r2[3]) and (r1[3] >= r2[1])
			v_overlaps = (r1[2] <= r2[4]) and (r1[4] >= r2[2])
			if h_overlaps and v_overlaps:
				return True
	return False
def pr(rects,cake):
	for x in rects:
		for q in range(x[1],x[3]+1):
			for r in range(x[2],x[4]+1):
				cake[q][r]=x[0]
	for x in range(0,len(cake)):
		cake[x]=''.join(cake[x])
	return '\n'.join(cake)
if __name__ == "__main__":
	testcases = input()
	for caseNr in xrange(1, testcases + 1):
		info = raw_input()
		print("Case #%i: %s" % (caseNr, solve(info)))
