case = int(raw_input())
cases = []
for i in range(case):
	row1 = int(raw_input())
	lines1 = []
	lines1.append(raw_input().split())
	lines1.append(raw_input().split())
	lines1.append(raw_input().split())
	lines1.append(raw_input().split())
	row2 = int(raw_input())
	lines2 = []
	lines2.append(raw_input().split())
	lines2.append(raw_input().split())
	lines2.append(raw_input().split())
	lines2.append(raw_input().split())
	count = 0
	selected = ""
	for e in lines1[row1-1]:
		if e in lines2[row2-1]:
			count += 1
			selected = e
	if count == 0:
		cases.append("Case #%d: Volunteer cheated!" % (i+1))
	elif count == 1:
		cases.append("Case #%d: %s" % ((i+1),selected))
	else:
		cases.append("Case #%d: Bad magician!" % (i+1))

for l in cases:
	print l

