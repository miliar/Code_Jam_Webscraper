T = int(input())
for t in range(T):
	sMax, shyStr = input().split()
	sMax = int(sMax)
	pplStanding = 0
	shyLvl = 0
	totalFriends = 0
	for digit in shyStr:
		digit = int(digit)
		if shyLvl <= pplStanding:
			pplStanding += digit
		else:
			reqdFrnds = shyLvl - pplStanding
			pplStanding += digit + reqdFrnds
			totalFriends += reqdFrnds
		shyLvl += 1
	print("case #", t + 1, ": ", totalFriends, sep = "")
