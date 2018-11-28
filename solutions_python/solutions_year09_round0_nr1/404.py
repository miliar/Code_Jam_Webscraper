import re

L,D,N = (int(s) for s in input().split())

words = [input() for _ in range(D)]

for n in range(1,N+1):
	test = re.findall(r'\([a-z]+\)|[a-z]', input())
	i = 0
	for word in words:
		if all(w in t for w,t in zip(word, test)):
			i += 1
	print('Case #%s: %s' % (n,i))
