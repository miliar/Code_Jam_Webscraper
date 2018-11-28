
def tidy(n):
	prev = 0
	pos = 0
	s = list(str(n))
	for c in s:
		curr = int(s[pos])
		if curr < prev:
			while curr < prev:
				pos-=1
				curr = prev-1
				if pos == 0:
					break
				prev = int(s[pos-1])
			s[pos] = str(curr)
			for j in range(pos+1,len(s)):
				s[j] = '9'
			return int("".join(s))
		else:
			prev = curr
			pos+=1
	return n

t = int(input())
for i in range(1, t + 1):
	n = input().split(" ")
	n = (int(n[0]))
	print("Case #{}: {}".format(i, tidy(n)))
