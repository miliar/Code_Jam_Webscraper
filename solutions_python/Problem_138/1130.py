def getJustGreater(needle, sortedHaystack):
	for x in sortedHaystack:
		if (x > needle):
			return x

	return None


def solve():
	N = int(input())

	naomi_weights = [float(x) for x in input().split()]
	ken_weights = [float(x) for x in input().split()]

	naomi_weights.sort()
	ken_weights.sort()

	# print(ken_weights)
	# print(naomi_weights)

	ken_weights_temp = ken_weights[:]
	naomi_weights_temp = naomi_weights[:]

	# Vanilla War #
	ken_win = 0
	naomi_win = 0

	for i in range(0, N):
		naomi_choice = max(naomi_weights)
		ken_choice = getJustGreater(naomi_choice, ken_weights)
		if ken_choice is None:
			ken_choice = min(ken_weights)
			naomi_win += 1
		else:
			ken_win += 1

		naomi_weights.remove(naomi_choice)
		ken_weights.remove(ken_choice)

	honest_win = naomi_win
	##

	ken_weights = ken_weights_temp[:]
	naomi_weights = naomi_weights_temp[:]

	# Deceitful War #
	ken_win = 0
	naomi_win = 0

	for i in range(0, N):
		ken_max = max(ken_weights)
		naomi_min = min(naomi_weights)

		naomi_choice = getJustGreater(ken_max, naomi_weights)
		if naomi_choice is None:
			naomi_weights.remove(naomi_min)
			ken_weights.remove(ken_max)
			ken_win += 1
		else:
			naomi_weights.remove(naomi_choice)
			ken_weights.remove(ken_max)
			naomi_win += 1

	cheat_win = naomi_win
	##

	print("Case #"+str(ct_case+1)+": "+str(cheat_win)+" "+str(honest_win))


T = int(input())
for ct_case in range(0, T):
	solve()