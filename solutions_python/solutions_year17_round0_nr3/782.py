n = int(input().strip())
for i in range(0, n):
	test = list(map(int, input().strip().split()))
	d = {}
	t = [test[0]]
	d[test[0]] = 1
	#count = 0
	j = 0
	'''
	for j in range(0, test[1]-1):
		tmp = max(t)
		t.remove(tmp)
		if tmp % 2 == 0:
			t.append(tmp//2)
			t.append((tmp// 2) - 1)
		else:
			t.append(tmp//2)
			t.append(tmp//2)
	if max(t) % 2 == 0:
		print("Case #{}: {} {}".format(i+1, max(t)//2, max(t)//2 -1))
	else:
		print("Case #{}: {} {}".format(i+1, max(t)//2, max(t)//2))
	'''	
	while j < test[1]-1:
		t = sorted(t)
		tmp = t[-1]
		times = d[t[-1]]
		if times + j < test[1]:
			t = t[:-1]
			if tmp % 2 == 0:
				if (tmp// 2) - 1 in t:
					d[(tmp// 2) - 1] += times
				else:
					t += [(tmp// 2) - 1]
					d[(tmp// 2) - 1] = times
				if tmp//2 in t:
					d[tmp//2] += times
				else:
					t += [tmp//2]
					d[(tmp// 2)] = times
			else:
				if tmp//2 in t:
					d[tmp//2] += times*2
				else: 
					t += [tmp//2]
					d[tmp//2] = times*2
		j += times
	t = sorted(t)
	if t[-1] % 2 == 0:
		print("Case #{}: {} {}".format(i+1, t[-1]//2, t[-1]//2 -1))
	else:
		print("Case #{}: {} {}".format(i+1, t[-1]//2, t[-1]//2))