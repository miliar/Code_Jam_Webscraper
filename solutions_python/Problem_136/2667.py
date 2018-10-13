T = int(input())
for CaseID in range(1,T+1):
	C,F,X = list(map(float,input().split()))
	sum = 0.
	R = 2. #cookies per second
	while True:
		t_C = C/R
		t_X = X/R
		t_Next = t_C + X/(R+F)
		R = R + F
		#print("t_C = %.3f , t_X = %.3f , t_Next = %.3f"%(t_C,t_X,t_Next))
		if t_Next > t_X:
			sum += t_X
			print("Case %d: %.7f" %(CaseID,sum))
			break;
		sum += t_C