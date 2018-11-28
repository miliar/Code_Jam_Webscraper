def to_bool(pancake):
	if pancake == "+":
		return True
	else: 
		return False

t = int(input())
cases = []
for i in range(t):
	cases.append(input())

for c in range(t):
	case = cases[c].split()
	pan = int(case[1])
	case = [to_bool(i) for i in case[0]]
	length = len(case)
	target = [True] * length
	moves = 0
	i = 0
	#while not (i > length-pan+1 or case == target):
	#	if not case[i]:
	#		moves += 1
	#		for j in range(i, i+pan-1):
	#			case[j] = not case[j]
	
	for i in range(length-pan+1):
		if not case[i]:
			moves += 1
			for j in range(i, i+pan):
				case[j] = not case[j]
	if case == target:
		print("Case #{}: {}".format(c+1, moves))
	else:
		print("Case #{}: IMPOSSIBLE".format(c+1))
