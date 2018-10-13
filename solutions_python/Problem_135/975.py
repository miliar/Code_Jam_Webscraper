#!/usr/bin/python3

t = int(input())
for i in range(t):
	ans1 = int(input())
	for j in range(4):
		line = input()
		if j == ans1-1:
			row1 = set(map(int, line.split()))
	ans2 = int(input())
	for j in range(4):
		line = input()
		if j == ans2-1:
			row2 = set(map(int, line.split()))
	ans = row1.intersection(row2)
	if not ans:
		out = 'Volunteer cheated!'
	elif len(ans) == 1:
		out = str(ans.pop())
	else:
		out = 'Bad magician!'

	print('Case #%d: %s' % (i+1, out) )
	
