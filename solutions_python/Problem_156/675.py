
from sys import argv

fname = argv[1]
f = open(fname, 'r')

content = f.read().split('\n')


ncases = int(content[0])

for ncase in range(1, 1 + ncases):
	
	ntables = int(content[ncase*2 -1])
	t_orig = content[ncase*2].split(' ')
	
	for i in range(len(t_orig)):
		t_orig[i] = int(t_orig[i])
	
	p_max = max(t_orig)
	steps_min = p_max
	
	for p_lim in range(1, p_max+1):
		#print(' ')
		#print(p_lim)
		t_cur = t_orig[:]
		
		n_steps = 0
		i = 0
		while (i < len(t_cur)):
			if t_cur[i] > p_lim:
				t_cur.extend([t_cur[i] - p_lim])
				t_cur[i] = p_lim
				n_steps += 1
			#print(t_cur)
			i += 1
		
		#print(p_max, max(t_cur), n_steps, max(t_cur)+n_steps)
		if (max(t_cur)+n_steps) < steps_min: steps_min = max(t_cur)+n_steps
	print('Case #%d: %d' % (ncase, steps_min))
		
	#print(ntables)
	#print(t_orig)
	#print(p_max)
	
	
	
	#print('Case #%d: %d' % (ncase, nfriends))