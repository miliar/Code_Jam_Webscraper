cases = int(raw_input())

for x in range(1,cases+1):
	vals = raw_input().split(' ')
	R = int(vals[0])
	origCap = int(vals[1])
	N = int(vals[2])
	
	groups = raw_input().split(' ')
	
	money = 0
	for run in range(R):
		cap = origCap
		boarded = 0
		while (int(groups[0]) <= cap and boarded<len(groups)):
			aGroup = int(groups.pop(0))
			cap -= aGroup
			groups.append(aGroup)
			money += aGroup
			boarded += 1
	
	print(('Case #%d: ' + str(money)) % x)
