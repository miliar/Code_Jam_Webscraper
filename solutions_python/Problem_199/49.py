
def flip(s,k):
	lst = [1 if s[i] == '+' else 0 for i in range(len(s))]
	ans = 0
	for i in range(len(s)-k+1):
		if lst[i] == 0:
			ans += 1
			for j in range(k):
				lst[i+j] = 1-lst[i+j]
	if min(lst) == 0:
		return -1
	return ans

t = int(raw_input())
for q in range(t):
	[s, k] = raw_input().split(' ')
	k = int(k)
	ans = flip(s,k)
	print "Case #" + str(q+1) + ": " + ("IMPOSSIBLE" if ans == -1 else str(ans))