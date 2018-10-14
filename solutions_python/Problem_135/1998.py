T = int(raw_input())
for i in range(T):
	n1 = int(raw_input())
	for j in range(4):
		dummy = map(int, raw_input().split())
		if j == n1 - 1:
			L1 = dummy
	n2 = int(raw_input())
	for j in range(4):
		dummy = map(int, raw_input().split())
		if j == n2 - 1:
			L2 = dummy
	rst = list(set(L1).intersection(L2))
	if len(rst) == 0:
		ans = "Volunteer cheated!"
	elif len(rst) == 1:
		ans = rst[0]
	else:
		ans = "Bad magician!"
	print "Case #%d: %s" % (i+1,ans)