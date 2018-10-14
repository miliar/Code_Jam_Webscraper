for t in range(int(input())):
	n,k = [int(i) for i in input().split()]
	elements = [1]
	for i in range(n):
		elements.append(0)
	elements.append(1)
	f = 0;l = n + 1;
	for i in range(k - 1):
		flag = 0
		m = (f + l) // 2
		elements[m] = 1
		co = 0;tempco = 0
		for j in range(n + 2):
			if elements[j] == 1:
				if co < tempco:
					co = tempco
					f = tempf
					l = templ
				tempco = 0
				tempf = j + 1
				templ = j
			else:
				tempco += 1
				templ += 1
	l = [-1]
	f = 0
	for i in range(1,n + 1):
		if elements[i] == 1:
			l.append(-1)
			f = 0
		else:
			l.append([f])
			f += 1
	la = 0
	for i in range(n,0,-1):
		if elements[i] == 1:
			la = 0
		else:
			l[i].append(la)
			la += 1
	minl = -1
	for i in range(n + 1):
		if l[i] != -1 and min(l[i][0],l[i][1]) > minl:
			minl = min(l[i][0],l[i][1])
	maxl = -1
	for i in range(n + 1):
		if l[i] != -1 and min(l[i][0],l[i][1]) == minl:
			if max(l[i][0],l[i][1]) > maxl:
				maxl = max(l[i][0],l[i][1])
	print('Case #{}: {} {}'.format(t + 1,maxl,minl))
