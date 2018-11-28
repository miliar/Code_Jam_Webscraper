def check_tidy(value):
	value = str(value)
	digits = [int(i) for i in value]
	for i in range(1, len(value)):
		if value[i-1] > value[i]:
			return False
	else:
		return True


t = int(input())
cases = []
for i in range(t):
	cases.append(input())

for c in range(t):
	case = int(cases[c])
	result = None
	for i in range(case, 0, -1):
		if check_tidy(i):
			result = i
			break
	print("Case #{}: {}".format(c+1, result))
