# def flip(s):
# 	S = ''
# 	for x in s:
# 		if(x =='+'):
# 			S = S + '-'
# 		else:
# 			S = S + '+'
# 	return S

# def is_good(s):
# 	return '-' not in s

f = open("pan.in", "r")
T = int(f.readline())

f2 = open("pan.out","w")
q = 0
for line in f:
	cakes = list(line.split(' ')[0])
	k = int(line.split(' ')[1])
	n = len(cakes)
	ans = 0
	# print(cakes, n, k)
	for i in range(n-k+1):
		if(cakes[i] == '-'):
			ans += 1
			for j in range(k):
				if(cakes[i+j] =='+'):
					cakes[i+j] = '-'
				else:
					cakes[i+j] = '+'
		# print(i, cakes[i:i+k])
	# print(cakes)
	if('-' in cakes):
		print("Case #{}: IMPOSSIBLE".format(q+1))
		f2.write("Case #{}: IMPOSSIBLE\n".format(q+1))
	else:
		print("Case #{}: {}".format(q+1, ans))
		f2.write("Case #{}: {}\n".format(q+1, ans))
	q += 1
f.close()
f2.close()