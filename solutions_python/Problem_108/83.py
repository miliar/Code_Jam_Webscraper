t = input()
for l in range(t):
    v = input()
    a = [0] * v
    b = [0] * v
    f = [0] * v
    for j in range(v):
	a[j], b[j] = map(int, raw_input().split(" "))
    d = input()
    if a[0] > b[0]:
	print "Case #%d: NO" % (l + 1)
	continue
    f[0] = a[0]
    nowj = 0
    nextj = 0
    nexth = 0
    suc = False
    for i in range(0, v):
	if f[i] + a[i] >= d:
	    suc = True
	    break
	for j in range(i + 1, v):
	    if f[i] + a[i] >= a[j]:
		if f[j] < min(a[j] - a[i], b[j]):
		    f[j] = min(a[j] - a[i], b[j])
	    else:
		break
    if suc:
	print "Case #%d: YES" % (l + 1)
    else:
	print "Case #%d: NO" % (l + 1)
