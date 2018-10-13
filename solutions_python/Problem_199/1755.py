def inverse(s):
	return ''.join(['+' if c == '-' else '-' for c in s])

def reverse(string, nStep, k):
	if(string == len(string)*'+'):
		return nStep
	else:
		for i in range(0, len(string)-k+1):
			if(string[i:i+k][0] == '-'):
				ns = string[:i] + inverse(string[i:i+k]) + string[i+k:]
				return reverse(ns, nStep+1, k)
		return 'IMPOSSIBLE'

import sys
if __name__ == '__main__':
	inputPath = sys.argv[1]
	outputPath = sys.argv[2]
	with open(inputPath, 'r') as f:
		with open(outputPath, 'w') as fout:
			text = f.read().splitlines()
			for i, l in enumerate(text):
				if(i == 0):
					continue
				else:
					s, k = l.split(' ')
					step = reverse(s, 0, int(k))
					fout.write('Case #{}: {}\n'.format(i, step))

	#t = int(input())
	#for i in range(1, t + 1):
	#	s, k = input().split(' ')
	#	step = reverse(s, 0, int(k))
	#	print('Case #{}: {}'.format(i, step))