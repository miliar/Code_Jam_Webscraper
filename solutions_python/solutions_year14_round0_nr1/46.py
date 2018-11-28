def qq(a, b):
	for i in range(0, 4):
		if a in b[i]:
			return i

tt = int(raw_input())
for t in range(1, tt + 1):
	r1 = int(raw_input()) - 1
	q1 = []
	q2 = []
	for i in range(0, 4):
		q1.append(map(int, raw_input().split()))
	r2 = int(raw_input()) - 1
	for i in range(0, 4):
		q2.append(map(int, raw_input().split()))
	ans = -1
	for i in range(1, 17):
		if r1 == qq(i, q1) and r2 == qq(i, q2):
			if ans == -1:
				ans = i
			else:
				ans = -2
	print "Case #" + str(t) + ": " + (str(ans) if ans > 0 else ("Bad magician!" if ans == -2 else "Volunteer cheated!"))
