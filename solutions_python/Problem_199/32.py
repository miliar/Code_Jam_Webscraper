def process(pancakes, K):
	N = len(pancakes)
	flips = 0
	for i in range(N):
		if pancakes[i] == '-':
			flips += 1
			for j in range(K):
				if i+j >= N:
					return -1
				pancakes[i+j] = '-' if pancakes[i+j] == '+' else '+'

	return flips

def run():
	T = int(raw_input().strip())
	for caseno in range(T):
		pancakes, Kstr = raw_input().strip().split()
		flips = process(list(pancakes), int(Kstr))
		print 'Case #' + str(caseno+1) + ':', (flips if flips >= 0 else 'IMPOSSIBLE')

run()