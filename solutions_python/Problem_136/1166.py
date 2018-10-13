def getTimeTo(target, rate, curr=0):
	if (curr < target):
		return (target-curr)/rate
	else:
		return 0.0

def solve():
	rate = 2.0
	time = 0.0

	[C, F, X] = [float(x) for x in input().split()]

	while(True):
		time_target = getTimeTo(X, rate)
		time_farm = getTimeTo(C, rate)

		if (time_target <= time_farm):
			time += time_target
			print("Case #"+str(ct_case+1)+": "+"%.7f"%time)
			return
		else:
			time_to_target_without_farm = getTimeTo(X, rate, time_farm*rate)
			time_to_target_with_farm = getTimeTo(X, rate+F)

			if (time_to_target_without_farm <= time_to_target_with_farm):
				out = time + time_farm + time_to_target_without_farm
				print("Case #"+str(ct_case+1)+": "+"%.7f"%out)
				return

			time += time_farm
			rate += F


T = int(input())
for ct_case in range(0, T):
	solve()