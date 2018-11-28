def do_case():
	# input()
	# int(input())
	n, p = list(map(int, input().split()))
	l = list(map(int, input().split()))
	m = [0 for _ in range(p)]
	for i in l:
		m[i%p] += 1

	# always take fulls
	out = m[0]
	m[0] = 0

	# then take all pairs of good, bad
	for x in range(1, (p+1)//2):
		q = min(m[x], m[p-x])
		out += q
		m[x] -= q
		m[p-x] -= q

	if p % 2 == 0:
		q = m[p//2] // 2
		out += q
		m[p//2] -= (m[p//2] // 2) * 2

	# print(m, p)

	# now we pick off the rest
	# somehow
	# oh we just hard code it
	if p == 2:
		if m[1]: out += 1
	if p == 3:
		# take 1s
		if m[1]:
			assert m[2] == 0
			out += (m[1] + 2) // 3
		if m[2]:
			assert m[1] == 0
			out += (m[2] + 2) // 3

		# out += m[1] // 3
		# out += m[2] // 3
	if p == 4:
		if m[1]:
			assert m[3] == 0
			if m[2]:
				# take 2x1, then take a 2
				if m[1] >= 2:
					m[1] -= 2
					m[2] = 0
					out += 1
			out += (m[1] + 3) // 4
		elif m[3]:
			assert m[1] == 0
			if m[2]:
				# take 2x1, then take a 2
				# if not, well ok
				if m[3] >= 2:
					m[3] -= 2
					m[2] = 0
					out += 1
			out += (m[3] + 3) // 4
		elif m[2]:
			# just take it
			out += 1

		# if m[2]: out += 1
		# out += m[1] // 4
		# out += m[3] // 4


	# out2 = 0
	# for x in range(1, p//2+1):
	# 	out2 += min(m[x], m[p-x])
	# out += out2

	# # always take full ones
	# out = 0
	# bad = []
	# for i in l:
	# 	if l % p == 0:
	# 		out += 1
	# 	else:
	# 		bad.append(i%p)


	return out

T = int(input())
for case in range(T):
	ans = do_case()
	print("Case #{}: {}".format(case+1, ans))
