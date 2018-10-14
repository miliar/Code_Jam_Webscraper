
import sys

import numpy as np

f = open(sys.argv[1], 'r')
lines = f.readlines()
f.close()

T = int(lines[0].strip())

of = open(sys.argv[1].split('.')[0]+'.out', 'w')
for case_i, case in enumerate(lines[1:]):
	F = 0
	i = 0

	case = case.strip().split()
	seq = np.array([{'-':0, '+':1}[c] for c in case[0]], dtype=bool)
	K = int(case[1])
	for i in range(len(seq) - (K - 1)):
		if seq[i] == 0:
			F += 1
			seq[i:i+K] = ~seq[i:i+K]

	of.write(f'Case #{case_i+1}: ')
	if np.all(seq == 1):
		of.write(f'{F}\n')
		print(case, F)
	else:
		of.write('IMPOSSIBLE\n')
		print(case, 'IMPOSSIBLE')

of.close()
