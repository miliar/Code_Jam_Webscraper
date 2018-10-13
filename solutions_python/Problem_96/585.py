max_score = 10
normal = {}
surprising = {}
for a in range(max_score+1):
	for b in range(max_score+1):
		for c in range(max_score+1):
			diff = max(abs(a-b), abs(b-c), abs(c-a))
			s = a + b + c
			p = max(a,b,c)
			if diff <= 1 and (s not in normal or normal[s] < p):
				normal[s] = p
			elif diff == 2 and (s not in surprising or surprising[s] < p):
				surprising[s] = p

T = int(input())
for i in range(1, T+1):
	n,s,p,*l = [int(i) for i in input().split()]
	cnt = 0
	for t in l:
		if t in normal and normal[t] >= p:
			cnt += 1
		elif t in surprising and surprising[t] >= p:
			if s > 0:
				s -= 1
				cnt += 1
	print("Case #", i, ": ", cnt, sep="")

