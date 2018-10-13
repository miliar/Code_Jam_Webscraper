def solve(caseId):
	n = input() - 1
	a = []
	for i in range(4):
		a += [map(int , raw_input().split())]
	m = input() - 1
	b = []
	for i in range(4):
		b += [map(int , raw_input().split())]
	ans = []
	for card in a[n]:
		if card in b[m]:
			ans += [card]
	cnt = len(ans)
	print "Case #" + str(caseId) + ":", 
	if cnt == 0:
		print "Volunteer cheated!"
	elif cnt == 1:
		print ans[0]
	else:
		print "Bad magician!"
t = input()
for i in range(t): solve(i+1)