def valid(x):
	y = [int(y) for y in list(str(x))]
	if len(y) == 1:
		return True, -1
	else:
		correct = True
		i = -1
		for j in range(1, len(y)):
			if y[j] < y[j-1]:
				correct = False
				i = j
				break
		return correct, i

cases = int(input())

for c in range(1,cases+1):
	raw = int(input())
	res = raw

	v, i = valid(res)
	while not v:
		extra = int(str(res)[i:]) + 1
		res -= extra
		v, i = valid(res)

	print("Case #", c, ": ", res, sep="")

