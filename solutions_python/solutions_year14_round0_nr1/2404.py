cases = int(raw_input())
for i in range(cases):
	rowca = int(raw_input())
	for j in range(4):
		if j == rowca-1:
			row1 = set(map(int, raw_input().split()))
		else:
			raw_input()
	rowcb = int(raw_input())
	for k in range(4):
		if k == rowcb-1:
			row2 = set(map(int, raw_input().split()))
		else:
			raw_input()
	res = row1.intersection(row2)
	if len(res) == 1:
		ans = res.pop()
	elif len(res) == 0:
		ans = "Volunteer cheated!"
	else:
		ans = "Bad magician!"

	print "Case #" + str(i+1) + ":", ans
