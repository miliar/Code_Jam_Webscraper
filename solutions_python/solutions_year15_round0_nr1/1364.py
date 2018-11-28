t = int(raw_input())
for _t in range(t):
	sum = 0
	ans = 0
	max,s = map(str,raw_input().split())
	for x in range(len(s)):
		if(x > sum):
			ans += x - sum
			sum = x
		sum += int(s[x])
	print("Case #" + str(_t + 1) + ": " + str(ans))
