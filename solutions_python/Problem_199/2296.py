with open('A-large.in', 'rb') as fin, open('out.txt', 'wb') as fout:
    n = int(fin.readline().strip())

    def flip(s):
    	r = ''
    	for c in s:
    		r += '+' if c == '-' else '-'
    	return r

    for case in range(1, n + 1):
		p, n = fin.readline().strip().split()
		n = int(n)

		c = 0
		i = 0
		while i < len(p) - n + 1:
			if p[i] == '-':
				c += 1
				p = p[:i] + flip(p[i:i + n]) + p[i + n:]
			i += 1

		if p.count('-') == 0:
			fout.write('Case #{}: {}\n'.format(case, c))
		else:
			fout.write('Case #{}: {}\n'.format(case, 'IMPOSSIBLE'))
