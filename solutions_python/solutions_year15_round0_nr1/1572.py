T = int(raw_input())

for i in range(1, T+1):
	tmp = raw_input().split()
	smax, si = int(tmp[0]), [int(j) for j in tmp[1]]
	ans = 0
	tot = 0
	for ind, k in enumerate(si):
		diff = 0
		if ind > tot:
			diff = ind - tot
		tot += k + diff
		ans += diff
	print "Case #" + str(i) + ": " + str(ans)




