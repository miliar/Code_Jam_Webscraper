# #anilkumarravuru
# T = int(raw_input())
# for t in range(T):
# 	D, N = map(int,raw_input().split())
# 	P = []
# 	for i in range(N):
# 		P += [map(int,raw_input().split())]
# 	P.sort()
# 	mintime = 0
# 	for i in range(N-1,-1,-1):
# 		if i == N-1:
# 			tim = (D - P[i][0])/(1.0*P[i][1])
# 		else:
# 			if P[i][1] <= P[i+1][1]:
# 				tim = (D - P[i][0])/(1.0*P[i][1])
# 			else:
# 				meet = (P[i+1][0]-P[i][0])/((P[i][1]-P[i+1][1])*1.0)
# 				pos = P[i][0] + (P[i][1]*tim)
# 				if pos > D:
# 					tim = (D - P[i][0])/(1.0*P[i][1])
# 				else:
# 					tim = mintime
# 		if tim >= mintime:
# 			mintime = tim
# 	# print D/mintime
# 	print("Case #{}: {}".format(t+1, D/mintime))



#anilkumarravuru
T = int(raw_input())
for t in range(T):
	D, N = map(int,raw_input().split())
	P = []
	for i in range(N):
		P += [map(int,raw_input().split())]
	P.sort()
	mintime = 0
	for i in range(N):
		tim = (D - P[i][0])/(1.0*P[i][1])
		if tim > mintime:
			mintime = tim
	print("Case #{}: {}".format(t+1, D/mintime))
