fo = open('big.txt','w')
with open('test.txt') as f:
	lines = f.readlines()
	lines = [_.strip() for _ in lines]
	t = int(lines[0])
	i = 1
	for it in range(t):
		d,n = [int(_) for _ in lines[i].split()]
		i+=1
		max_time = 0.0
		for n_ in range(n):
			k,s = [int(_) for _ in lines[i].split()]
			i+=1
			time = (d-k)/float(s)
			max_time = max(time, max_time)
		fo.write('Case #{}: {:.6f}\n'.format(it+1, d/max_time))
fo.close()