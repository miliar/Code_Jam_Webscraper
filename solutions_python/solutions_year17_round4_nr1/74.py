import math

T = int(input())

for j in range(T):

	N, P = map(int, input().split(" "))
	G = list(map(int, input().split(" ")))
	G = list(map(lambda x: x % P, G))
	G.sort()

	# print(G)

	# If P <= 3, only 0,1,2 in G
	ans = G.count(0)

	if P == 2:
		ans += (G.count(1) + 1) // 2
	if P == 3:
		ans += min(G.count(1), G.count(2))
		ans += (abs(G.count(1)-G.count(2)) + 2) // 3


	print("Case #" + str(j+1) + ": " + str(ans))



