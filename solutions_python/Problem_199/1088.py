sign_change = {	"-": "+",
				"+": "-"}
loops = range(1, int(raw_input()) + 1)
for loop in loops:
	row, k = raw_input().split()
	k = int(k)
	row = list(row)
	flips, index = 0, 0
	place_max = len(row) - k
	k = range(k)
	while(True):
		if "-" not in row:
			print "Case #{}: {}".format(loop, flips)
			break
		if row.count("-") == 1:
			print "Case #{}: IMPOSSIBLE".format(loop)
			break
		for place, sign in enumerate(row):
			if sign == "-" and place <= place_max:
				for i in k:
					row[place + i] = sign_change[row[place + i]]
				flips += 1
				break
		else:
			print "Case #{}: IMPOSSIBLE".format(loop)
			break
