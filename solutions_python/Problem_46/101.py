

inf = float("infinity")

def count(s):
	l = list(s)
	l.reverse()
	cnt = 0
	for c in l:
		if c=='0': cnt += 1
		else: break
	return cnt



def fin(l):
	for i in range(len(l)):
		if l[i]>i: return False
	return True


def moveup(l,i):
	#print("# "+str(l)+","+str(i))
	if fin(l):
		return 0
	if i>=len(l):
		return inf
	best = moveup(list(l),i+1)
	#bnl = []
	for j in range(i):
		nl = list(l)
		nl.insert(j,nl.pop(i))
		swaps = (i-j)+moveup(nl,i+1)
		best = min(best,swaps)
		if best==swaps:
			bnl = nl
	#print(str(l)+","+str(i)+" has best "+str(bnl))
	return best


T = int(input())

for X in range(1,T+1):
	
	swaps = 0
	N = int(input())
	lines = []
	for r in range(N):
		lines += [max(input().rfind("1"),0)]
	
	#print(fin(lines))
	
	swaps = moveup(lines,1)
	
	print("Case #"+str(X)+": "+str(swaps))



















