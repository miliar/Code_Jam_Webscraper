T = int(raw_input())
for t in range(1,1+T):
	L, X = raw_input().split(' ')
	L = int(L)
	total = 0
	invited = 0
	for i in range(L+1):
		invited += max(i-total,0)
		total = max(total, i) + int(X[i])
	print("Case #%s: %s" % (t, invited) )
