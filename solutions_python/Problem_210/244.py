import math
testcase_count = int(input())

for testcase_index in range(testcase_count):
	ac, aj = map(int, input().split())
	c = []
	for i in range(ac):
		c.append(list(map(int, input().split())))
	j = []
	for i in range(aj):
		j.append(list(map(int, input().split())))
	
	if ac == 2 or aj == 2:
		t = c if ac == 2 else j
		t.sort(key=lambda a: a[0])
		if t[0][0] + 720 >= t[1][1] or t[1][0] + 720 >= t[0][1] + 1440:
			result = 2
		else:
			result = 4
	else:
		result = 2

	print("Case #%d: %d" % (testcase_index + 1, result))

