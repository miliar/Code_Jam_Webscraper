
# python 3.0




dirs = [(-1,0),(0,-1),(0,1),(1,0)]
def drain(alts, coord):
	H,W = len(alts),len(alts[0])
	h,w = coord
	nebs = [10001 for d in dirs]
	for i in range(4):
		d = dirs[i]
		dh,dw = d
		nh,nw = h+dh,w+dw
		if 0<=nh<H and 0<=nw<W:
			nebs[i] = alts[nh][nw]
	mini = min(nebs)
	#print("mini "+str(mini))
	if not mini<alts[h][w]:
		return (0,0)
	else:
		for i in range(4):
			if nebs[i] == mini:
				return dirs[i]


T = int(input())

for X in range(1,T+1):
	print("Case #"+str(X)+":")
	
	H,W = [int(v) for v in input().split()]
	
	alts = [[int(a) for a in input().split()] for h in range(H)]
	
	draindirs = [[drain(alts,(h,w)) for w in range(W)] for h in range(H)]
	
	drains = [[(h+draindirs[h][w][0] , w+draindirs[h][w][1]) for w in range(W)] for h in range(H)]
	
	
	basinids = [[0 for w in range(W)] for h in range(H)]
	cid = 1
	for h in range(H):
		for w in range(W):
			if drains[h][w]==(h,w):
				basinids[h][w] = cid
				cid += 1
	
	left = True
	while(left):
		left = False
		for h in range(H):
			for w in range(W):
				ph,pw = drains[h][w]
				basinids[h][w] = basinids[ph][pw]	# propagate upwards
				if basinids[h][w]==0:
					left = True
	
	basins = [["X" for w in range(W)] for h in range(H)]
	letters = list('abcdefghijklmnopqrstuvwxyz')
	idl = [None for i in range(cid)]
	for h in range(H):
		for w in range(W):
			idi = basinids[h][w]
			if not idl[idi]:
				idl[idi] = letters.pop(0)
			basins[h][w] = idl[idi]
	
	
	#for line in alts: print(" ".join([str(a) for a in line]))
	#for line in drains: print(" ".join([str(a) for a in line]))
	#for line in basinids: print(" ".join([str(a) for a in line]))
	for line in basins: print(" ".join([str(a) for a in line]))
	































