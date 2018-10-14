import math

for L in range(int(input())):
	N,K = [t(s) for t,s in zip((int,int),input().split())]
	
	area_top = []
	area_side = []
	for _ in range(N):
		R,H = [t(s) for t,s in zip((int,int),input().split())]
		area_top.append(R*R*math.pi)
		area_side.append(2*R*math.pi*H)
		#print("top",area_top[-1],"side",area_side[-1],"R",R,"H",H)
	
	best = 0
	for bot in range(N):
		#just try all bottoms
		avail_sides = []
		for i,(top,side) in enumerate(zip(area_top,area_side)):
			if i==bot: continue
			if top>area_top[bot]: continue
			avail_sides.append(side)
		avail_sides = sorted(avail_sides, reverse=True)
		this = area_top[bot] + area_side[bot] + sum(avail_sides[0:K-1])
		#print(L+1, this, bot, avail_sides, list(avail_sides[0:K-1]))
		if this > best:
			best = this
	print("Case #"+str(L+1)+": "+str(best))
