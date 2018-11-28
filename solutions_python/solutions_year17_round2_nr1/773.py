T = int(input())

for t in range(T):
	D, N = list(map(int,input().split()))
	horses = []
	for i in range(N):
		Ki, Si = list(map(int,input().split()))
		distance = D - Ki
		time = distance*1.0 / Si
		horses.append(time)
	maxtime = max(horses)

	maxvit = 1.0*D / maxtime


	print("Case #" + str(t+1) + ": " + str(maxvit))