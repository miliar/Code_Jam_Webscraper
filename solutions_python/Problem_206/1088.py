import sys

t = int(input())
for tc in range(t):
	d,n = [int(x) for x in input().split()]
	slowest_d = d
	slowest_v = 100
	for _ in range(n):
		s, v = [int(x) for x in input().split()]
		rem_time = (d - s)/v
		if rem_time > (d - slowest_d)/slowest_v:
			slowest_v = v
			slowest_d = s
	t = (d - slowest_d) / slowest_v
	fastest_v = d / t
	print("Case #{0}: ".format(tc+1), end = '')
	print("%.6f" % fastest_v)
	sys.stdout.flush()