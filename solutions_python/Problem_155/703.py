t = int(raw_input())
def process(case):
	n, st = raw_input().split()
	n = int(n)
	cnt = 0
	ans = 0
	for i in range(n + 1):
		if cnt < i:
			ans += i - cnt
			cnt = i
		cnt += int(st[i])

	print "Case #" + str(case) + ":" , ans

for i in range(t):
	process(i + 1)
