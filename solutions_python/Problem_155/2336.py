f = open('A-small-attempt1.in');

cases = int(f.readline())

for num in range(1, cases+1):
	case = f.readline().split(" ")[1].rstrip()
	clapping = 0
	extra = 0

	for s,x in enumerate(case):
		if s <= clapping:
			clapping += int(x)
		else:
			if int(x) != 0:
				diff = s - clapping
				extra += diff
				clapping += diff + int(x)

	print("Case #", num, ": ", extra, sep="")