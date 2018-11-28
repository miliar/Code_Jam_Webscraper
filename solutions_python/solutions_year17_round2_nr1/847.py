t = int(raw_input())

for x in range(1, t + 1):
	d, n = map(int, raw_input().split(' '))
	worst = 0
	for i in range(n):
		k, s = map(int, raw_input().split(' '))
		time = (d - k) / float(s)
		worst = max(time, worst)
	y = d / float(worst)
	print("Case #%d: %.6f"%(x, y))

