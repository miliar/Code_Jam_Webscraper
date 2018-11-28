v = ["a", "e", "i", "o", "u"]


def substrings(s):
	lst = [""]
	for start in range(0, len(s)):
		for end in range(start, len(s)):
			lst.append(s[start:end+1])
	return lst

def has(n, m):
	for i in range(0, len(n)):
		x = 0
		j = i
		while j < len(n) and n[j] not in v:
		    x += 1
		    j += 1
		if x >= m:
		    return True
	return False 


T = int(raw_input())
c = 0
while T > 0:
	c += 1
	d = raw_input().split(" ")
	s = d[0]
	n = int(d[1])
	res = 0
	q = substrings(s)
	for i in q:
		if has(i, n):
			res += 1
	print("Case #%d: %d" % (c, res))
	T -= 1




