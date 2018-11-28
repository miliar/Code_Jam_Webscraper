t = int(raw_input())
for i in range(1,t+1):
	print "Case #%d:" %i,
	r1 = int(raw_input())
	r,c = [],[]
	for i in range(4):
		r.append(raw_input().split())
	r = r[r1-1]
	r2 = int(raw_input())
	for i in range(4):
		c.append(raw_input().split())
	c = c[r2 -1]
	ans = [x for x in r if x in c]
	if len(ans) == 1:
		print ans[0]
	elif len(ans) == 0:
		print "Volunteer cheated!"
	else:
		print "Bad magician!"