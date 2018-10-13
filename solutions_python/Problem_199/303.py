
def calc(lst, k):
	def check(lst, k):
		if len(lst) <= k and len(set(lst)) == 1:
			return True, (0 if lst[0] == 1 else 1)
		i = 0
		cnt = 0
		while i < len(lst) - k + 1:
			if lst[i] == 0:
				for j in xrange(i, min(i+k, len(lst))):
					lst[j] = not lst[j]
				cnt += 1
			i += 1
		return (False if len(set(lst)) != 1 else True), cnt


	ret, cnt = check(lst, k)
	if not ret:
		return "IMPOSSIBLE"
	return cnt




t = input()
for i in xrange(t):
	s, k = raw_input().split()
	lst = [1 if c == '+' else 0 for c in s]
	print "Case #%d:" % (i+1), calc(lst, int(k))