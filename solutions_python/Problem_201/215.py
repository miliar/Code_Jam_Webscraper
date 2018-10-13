def BathroomStall(N,K):
	curA = {N:1}
	toFill = K
	curPower = 0
	while True:
		curLayer = pow(2,curPower)
		if curLayer < toFill:
			nextA = {}
			for space in curA:
				if space % 2 == 0:
					lv = (space//2)-1
					mv = space//2
					if lv not in nextA:
						nextA[lv] = 0
					if mv not in nextA:
						nextA[mv] = 0

					nextA[lv] += curA[space]
					nextA[mv] += curA[space]
				else:
					ev = (space-1)//2
					if ev not in nextA:
						nextA[ev] = 0
					nextA[ev] += 2*curA[space]
			curA = nextA
			toFill -= curLayer
			curPower += 1
		else:
			for space in sorted(curA,reverse=True):
				if toFill <= curA[space]:
					if space == 1:
						return "0 0"
					elif space %2 == 0:
						lv = (space//2)-1
						mv = space//2
						return str(mv)+" "+str(lv)
					else:
						ev = (space-1)//2
						return str(ev)+" "+str(ev)
				else:
					toFill -= curA[space]
	return "Unexpected thing occurred"

T = int(input())
for t in range(1,T+1):
	N,K = tuple(map(int,input().split()))
	print("Case #"+str(t)+": "+BathroomStall(N,K))