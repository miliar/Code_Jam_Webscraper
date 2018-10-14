#anilkumarravuru
T = int(raw_input())
for t in range(T):
	m, s = map(str,raw_input().split())
	r = int(s)
	l = list(m)
	count = 0
	for i in range(len(l)-r):
		if l[i]=='-':
			count += 1
			for j in range(r):
				if l[i+j] == '+':
					l[i+j] = '-'
				else:
					l[i+j] = '+'
			# print l
	if '-' not in l[-r:]:
		print("Case #{}: {}".format(t+1, count))
	elif '+' not in l[-r:]:
		print("Case #{}: {}".format(t+1, count+1))
	else:
		print("Case #{}: IMPOSSIBLE".format(t+1))

