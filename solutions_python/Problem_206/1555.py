from decimal import *

t = int(input())

for case in range(1,t+1):
	d,n = [int(x) for x in input().split()]
	arr = [[Decimal(x) for x in input().split()] for i in range(n)]
	mx = max((d-x[0])/x[1] for x in arr)
	print("Case #%d: %f" % (case, d/mx))