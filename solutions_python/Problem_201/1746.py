ifile = 'C-small-1-attempt0.in'
ofile = 'C_s.txt'


out = open(ofile, 'w')

def choose(ind):
	diff = [ind[i] - ind[i-1] for i in range(1, len(ind))]
	i = diff.index(max(diff))
	j = (ind[i] + ind[i+1]) / 2
	ind.insert(i+1, j)
	return ind, i+1


with open(ifile, 'r') as f:
	T = int(f.readline())
	for j in range(1, T+1):
		out.write('Case #%s: ' % j)

		n, k = f.readline().split()
		n = int(n)
		k = int(k)
		selected = [0, n+1]
		last_index = 0

		for i in range(k):
			selected, last_index = choose(selected)

		l = selected[last_index] - selected[last_index-1] - 1
		r = selected[last_index+1] - selected[last_index] - 1

		out.write('%s %s\n' % (max(l, r), min(l, r)))
		

out.close()

