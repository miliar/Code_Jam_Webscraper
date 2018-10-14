from math import ceil

def calc(A, d):
	total = sum(map(lambda c : int(ceil( float(c) / d ) ), A))
	total -= len(A)
	total += d
	return total

def process(case):
	ans = 0xCAFEBABE
	d = int(raw_input())
	A = map(int , raw_input().split())
	top = max(A)
	for d in range(1, top + 1):
		total = calc(A, d)
		if total < ans:
			ans = total
	print "Case #" + str(case) + ":" , ans

t = int(raw_input())
for i in range(t):
	process(i + 1)
