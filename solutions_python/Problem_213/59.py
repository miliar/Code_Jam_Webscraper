import math

T = int(input())

for j in range(T):

	N, C, M = map(int, input().split(" "))

	tickets = []
	C_count = [] # count of tickets by customer
	P_count = [] # count of tickets by position
	for i in range(C):
		C_count.append(0)
	for i in range(N):
		P_count.append(0)
	for i in range(M):
		P, B = map(int, input().split(" ")) # P = position [1..N]
		tickets.append([P, B])
		C_count[B-1] += 1
		P_count[P-1] += 1

	sum_P = 0
	min_trian = 0 
	for i in range(N):
		sum_P += P_count[i]
		min_trian = max((sum_P+i)//(i+1), min_trian)

	min_trian = max(max(C_count), min_trian)

	# print(min_trian)

	min_promo = 0

	for i in range(N):
		min_promo += max(0, P_count[i] - min_trian)


	print("Case #" + str(j+1) + ": " + str(min_trian) + " " + str(min_promo))



