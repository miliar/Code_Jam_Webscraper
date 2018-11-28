from sys import stdin

N_INDEX = 0 # number of googlers
S_INDEX = 1 # number of suprise triplets
P_INDEX = 2 # top score
START_INDEX = 3

def main():
	cases = int(stdin.readline())
	lines = stdin.readlines()
	for i in range(len(lines)):
		values = lines[i].split()
		N = int(values[N_INDEX])
		s = int(values[S_INDEX])
		p = int(values[P_INDEX])
		min_total = p
		if p > 2:
			min_total = 2 * (p - 2) + p

		print 'Case #{}:'.format(i+1),
		num_best = 0
		for googler in range(N):
			total_score = int(values[START_INDEX + googler])
			if (total_score >= min_total):
				if (3 * (p - 1) < total_score):
					num_best += 1
				elif (s):
					num_best += 1
					s -= 1
		print num_best

if __name__ == '__main__':
  main()
