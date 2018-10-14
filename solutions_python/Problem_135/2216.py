f = open('./A-small-attempt0.in', 'r')
fout = open('./magic.out', 'w')
numCases = int(f.readline())
for i in range(numCases):
	ans1 = int(f.readline())
	arr1 = []
	for j in range(4):
		arr1.append(f.readline().split())
	cand1 = arr1[ans1-1]

	ans2 = int(f.readline())
	arr2 = []
	for j in range(4):
		arr2.append(f.readline().split())
	cand2 = arr2[ans2-1]

	ans = []
	for num in cand1:
		if num in cand2:
			ans.append(num)
	if len(ans) == 0:
		print >> fout, "Case #%d: Volunteer cheated!" % (i+1)
	elif len(ans) == 1:
		print >> fout, "Case #%d: " % (i+1) + ans[0]
	else:
		print >> fout, "Case #%d: Bad magician!" % (i+1)

