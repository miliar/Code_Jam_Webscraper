T = int(input())
for t in range(1,T+1): 
	Ac,Aj = map(int,input().split())
	C = [list(map(int,input().split())) for _ in range(Ac)]
	J = [list(map(int,input().split())) for _ in range(Aj)]
	C.sort()
	J.sort()
	if Ac == 2:
		if C[1][1] - C[0][0] <= 720 or 1440 + C[0][1] - C[1][0] <= 720:
			answer = 2
		else:
			answer = 4
	elif Aj == 2:
		if J[1][1] - J[0][0] <= 720 or 1440 + J[0][1] - J[1][0] <= 720:
			answer = 2
		else:
			answer = 4
	else:
		answer = 2		
	print('Case #{}: {}'.format(t,answer))