def Solve():
	R, k, N = map(int, raw_input().split())
	groups = list(enumerate(map(int, raw_input().split())))
	used = set()
	money = []
	res = 0
	while groups[0][0] not in used:
		used.add(groups[0][0])
		if groups[0][1] > k:
			return sum(money)
		start = groups[0][0]
		total = 0
		coaster = []
		while len(groups) and total + groups[0][1] <= k:
			total += groups[0][1]
			coaster.append(groups[0])
			groups.pop(0)
		money.append((start, total))
		groups += coaster
	#print money
	while groups[0][0] != money[0][0]:
		res += money[0][1]
		R -= 1
		money.pop(0)
	#print money
	res += sum(m[1] for m in money)*(R/len(money))
	for i in range(R%len(money)):
		res += money[i][1]
	return res

for tc in range(1, int(input()) + 1):		
	print("Case #%d: %d" % (tc, Solve()))