import copy
f = open("C.in")
g = open("Cout2.txt","w")
T = int(f.readline())
for t in range(T):
	case = "Case #" + str(t + 1) + ": "
	N,K = map(int,f.readline().split())
	d = {N : 1}
	i = 1
	n = K
	'''
	if K > N / 2:
		g.write(case + "0 0" +"\n")
		continue
	'''
	while n > 0:
		a = max(d)
		if n - d[a] > 0:
			n = n - d[a]
			if a % 2 == 1:
				a2 = (a - 1) // 2
				if a2 in d:
					d[a2] = d[a2] + d[a] * 2
				else:
					d[a2] = d[a] * 2
			else:
				a2 = a // 2
				a3 = (a - 2) // 2
				if a2 in d:
					d[a2] = d[a2] + d[a]
				else:
					d[a2] = d[a]
				if a3 in d:
					d[a3] = d[a3] + d[a]
				else:
					d[a3] = d[a]
			d.pop(a)
		else:
			if a == 1:
				g.write(case + "0 0" +"\n")
			elif a % 2 == 0:
				g.write(case + str(a // 2) + " " + str((a - 2) // 2) +"\n")
			else:
				x = str((a-1) // 2)
				g.write(case + x + " " + x +"\n")
			break

	