T = int(raw_input())
k = 0
while k < T:
	k += 1
	r = int(raw_input())
	l = []
	for i in range(4):
		l.append(map(int, raw_input().split()))
	rl = l[r-1]
	r = int(raw_input())
	l = []
	for i in range(4):
		l.append(map(int, raw_input().split()))
		
	rl2 = l[r-1]
	ans = []
	for i in rl:
		for j in rl2:
			if i == j:
				ans.append(i)
	if (len(ans) == 1):
		print "Case #%s: %s" % (k, ans[0])
	elif (len(ans) > 1):
		print "Case #%s: Bad magician!" % k
	else :
		print "Case #%s: Volunteer cheated!" % k