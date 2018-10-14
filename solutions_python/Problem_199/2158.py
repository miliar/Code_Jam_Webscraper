cases = int(raw_input())
for h in range(cases):
	values = raw_input().split(" ")
	sal = [x for x in values[0]]
	flipper = values[1]
	counter = 0
	index = 0
	while index <= len(sal) - int(flipper):
		if sal[index] == "-":
			for k in range(int(flipper)):
				sal[index+k] = "+" if sal[index+k] == "-" else "-"
			counter += 1
		index += 1
	if "-" in sal:
		counter = "IMPOSSIBLE"
	print("Case #{0}: {1}".format(h+1,counter))