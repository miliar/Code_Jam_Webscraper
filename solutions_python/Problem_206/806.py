tc = int(input())

for cc in range(1, tc+1):
	d, n = [int(q) for q in input().split()]
	horses = []
	for i in range(n):
		horse = [int(q) for q in input().split()]
		horses.append(horse)

	maxtime = 0
	for horse in horses:
		time = (d - horse[0]) / horse[1]
		if time > maxtime:
			maxtime = time
			continue

	output = d / maxtime

	print("Case #{}: {}".format(cc, output))

