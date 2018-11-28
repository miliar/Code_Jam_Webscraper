t = int(input())

for case in range(1,t+1):
	n, p = [int(x) for x in input().split()]
	arr = [int(x) % p for x in input().split()]
	cnt = [sum(1 for x in arr if x==i) for i in range(p) ]
	if p == 2:
		ans = cnt[0] + (cnt[1] + 1)//2
	elif p == 3:
		ans = cnt[0]
		tmp = min(cnt[1], cnt[2])
		cnt[1] -= tmp
		cnt[2] -= tmp
		ans += tmp
		ans += (cnt[1]+2)//3 + (cnt[2]+2)//3
	print("Case #%d: %d" % (case, ans))