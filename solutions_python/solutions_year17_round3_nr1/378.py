import math

t = int(input())

for c in range(t):
    pks = []
    N,K = map(int,input().split())
    for i in range(N):
        r,h = map(int,input().split())
        pks.append((r,h))
    pks = sorted(pks,key=lambda x:x[0]*x[1])
    km1 = pks[N-K+1:]
    rest = pks[:N-K+1]
    rref = 0
    if km1:
        rref = max(km1,key=lambda x:x[0])[0]
    lastPk = (0,0)
    lastPkC = 0
    for p in rest:
        added = p[0]*p[1]*math.pi*2
        if p[0] > rref:
            added += math.pi *(p[0]-rref)**2
        if added > lastPkC:
            lastPk = p
            lastPkC = added
    km1.append(lastPk)
    total = 0
    for p in km1:
        total += p[0]*p[1]*math.pi*2
    rref = max(km1,key=lambda x:x[0])[0]
    total += math.pi * rref**2
    print("Case #%s: %.10f"%(c+1,total))





# pstr, k = input().split()
# k = int(k)
# size = len(pstr)
# pstr = [a == "+" for a in pstr]
# 
# i = 0
# flips = 0
# while i <= size-k:
# 	if not pstr[i]:
# 		flips += 1
# 		for j in range(i, i+k):
# 			pstr[j] = not pstr[j]
# 	i += 1
# 
# print("Case #%d: " % (c+1), end="")
# ok = True
# for x in range(size-k, size):
# 	if not pstr[x]:
# 		print("IMPOSSIBLE")
# 		ok = False
# 		break
# if ok:
# 	print(flips)

