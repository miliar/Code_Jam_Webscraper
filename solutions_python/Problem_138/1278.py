import sys
from copy import deepcopy

in_file = open(sys.argv[1], 'r')
out_file = open(sys.argv[2], 'w')

T = int(in_file.readline())

for i in range(T):
	N = int(in_file.readline())
	line = in_file.readline().split()
	naomi = []
	for n in line:
		naomi.append(float(n))
	line = in_file.readline().split()
	ken = []
	for n in line:
		ken.append(float(n))
	
	naomi.sort()
	ken.sort()
	l_naomi = len(naomi)
	l_ken = len(ken)
	low = 0
	high = l_naomi
	
	for n in naomi:
		if n < ken[0]:
			low += 1
		else:
			break
	for n in reversed(naomi):
		if n > ken[l_ken-1]:
			high -= 1
		else:
			break
	
	# War
	blocks_naomi = deepcopy(naomi)
	blocks_ken = deepcopy(ken)
	w_score = 0
	for i in range(l_naomi-1, -1, -1):
		if blocks_naomi[i] > blocks_ken[i]:
			w_score += 1
			blocks_naomi.pop()
			blocks_ken.pop(0)
		else:
			for j in range(len(blocks_ken)):
				if blocks_ken[j] > blocks_naomi[i]:
					blocks_ken.pop(j)
					blocks_naomi.pop()
					break
	
	# Deceitful War
	blocks_naomi = deepcopy(naomi)
	blocks_ken = deepcopy(ken)
	d_score = 0
	for i in range(low):
		blocks_naomi.pop(0)
		blocks_ken.pop()
		low -= 1
		high -= 1
	for i in range(high):
		block = blocks_naomi.pop(0)
		high -= 1
		if blocks_ken[0] < block:
			blocks_ken.pop(0)
			d_score += 1
		else:
			blocks_ken.pop()
	
	d_score += len(blocks_naomi) - high
	
	out_file.write('Case #{0}: {1} {2}\n'.format(i+1, d_score, w_score))

in_file.close()
out_file.close()
