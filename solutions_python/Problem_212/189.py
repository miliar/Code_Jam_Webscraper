def solve(n,p,g,db):
	mods = [0 for i in xrange(p)]
	for i in g:
		mods[i%p] +=1
	ans = mods[0]
	if(p==2):
		return ans + mods[1]/2 + mods[1]%2
	if(p==3):
		mi = min(mods[1],mods[2])
		mods[1]-=mi
		mods[2]-=mi
		ans +=mi
		def nonz(x):
			if(x%3==0):
				return 0
			return 1
		return ans + mods[1]/3 + mods[2]/3 + nonz(mods[1])+nonz(mods[2])
	
	#p==4
	x=mods[1]
	y=mods[2]
	z=mods[3]
	best = [[[0 for i in xrange(z+1)]for j in xrange(y+1)]for k in xrange(x+1)]
	deltas = [[1,0,1],[2,1,0],[0,1,2],[4,0,0],[0,0,4],[0,2,0]]
	totb = 0
	for i in xrange(x+1):
		for j in xrange(y+1):
			for k in xrange(z+1):
				for d in deltas:
					di = i-d[0]
					dj=j-d[1]
					dk=k-d[2]
					if(di>=0 and dj >= 0 and dk >= 0):
						best[i][j][k]=max(best[i][j][k],best[di][dj][dk]+1)
				if i==x and j==y and k==z:
					totb =max(totb, best[i][j][k])
				else:
					totb = max(totb, best[i][j][k]+1)
	return totb+ans

T = int(input())
for case in range(1,T+1):
	n,p=map(int,raw_input().split())
	g=map(int,raw_input().split())
	if T==7:
		db=True
	else:
		db=False
	print("Case #{}: {}".format(case, solve(n,p,g,db)))
