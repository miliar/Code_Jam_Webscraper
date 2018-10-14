t = int(raw_input())

for i in xrange(t):
	n1 = int(raw_input()) - 1
	alist1 = []
	for j in xrange(4):
		alist1.append([int(x) for x in raw_input().split()])
	n2 = int(raw_input()) - 1
	alist2 = []
	for k in xrange(4):
		alist2.append([int(x) for x in raw_input().split()])
	s1 = set(alist1[n1]).intersection(set(alist2[n2]))
	ans = ""
	if len(s1) > 1:
		ans = "Bad magician!"
	elif len(s1) == 0:
		ans = "Volunteer cheated!"
	else:
		ans = str(s1.pop())
	print "Case #%d: " %(i+1) + ans