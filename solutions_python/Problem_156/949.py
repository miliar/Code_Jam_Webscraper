filename = 'BS5'
fin = open(filename+'.in', 'r')
fout = open(filename+'.out', 'w')

def time2eat(l:list):
	ma = max(l) + 1
	T = [] * ma
	T.append([])
	T[0].append(l)
	i = 1
	while i <= ma:
		T.append([])
		for j in range(2**i):
			tmp = []
			if j % 2 == 0:
				tmp = [a-1 for a in T[i-1][int(j/2)] if a-1>0]
			else:
				tmp = T[i-1][int(j/2)]
				mi = tmp.index(max(tmp))
				m2 = int(tmp[mi] / 2) if (tmp[mi]%2==0) else int(tmp[mi] / 2 +1)
				if tmp[mi] == 9:
					m2 = 3
				tmp.append(m2)
				tmp[mi] = tmp[mi] - m2
			if sum(tmp) == 0:
				return i
			T[i].append(tmp)
		i += 1
	return 0

for i in range(int(fin.readline().strip())):
	d = int(fin.readline().strip())
	tmp = [int(a) for a in fin.readline().strip().split(' ')]
	time = time2eat(tmp)
	fout.write('Case #'+str(i+1)+': '+str(time)+'\n')

fout.close()
fin.close()