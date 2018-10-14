t_no = int(input())

for t in range(1, t_no + 1):
	d, n = [int(x) for x in input().split()]
	mx = 0
	for i in range(n):
		pos, v = [int(x) for x in input().split()]
		mx = max(mx, (d - pos) / v)
	print("Case #", t, ": ", d / mx, sep='') 
