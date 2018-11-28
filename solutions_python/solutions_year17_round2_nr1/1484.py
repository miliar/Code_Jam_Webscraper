T = int(input())
for t in range(1,T+1):
	D, N = map(int,input().split())
	H = [list(map(int,input().split())) for n in range(N)]
	S = [(D - h[0])/float(h[1]) for h in H]
	S.sort()
	answer = D/S[-1]
	print('Case #{}: {}'.format(t,answer))