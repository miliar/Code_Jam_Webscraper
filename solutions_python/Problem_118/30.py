F = open("Clog.txt")
P = []
S = set()
while True:
	l = F.readline()
	if l=="":
		break
	t = int(l[:-1].split()[1])
	if t not in S:
		P += [t]
		S.add(t)
#print len(P)
T = input()
for t in range(T):
	A,B = map(int,raw_input().split())
	ans = 0
	for p in P:
		if A<=p<=B:
			ans += 1
	print "Case #%s: %s"%(t+1,ans)
