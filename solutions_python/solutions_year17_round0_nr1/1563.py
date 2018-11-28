import random

def flip(stove, i, k):
	for x in xrange(k):
		stove[i+x] = not stove[i+x]

def generate(n, k):
	stove = [True] * n
	flips = 10000
	for _ in xrange(flips):
		f = random.randint(0, n-k)
		flip(stove, f, k)
	return stove, flips

def ltr(stove, k, cutoff):
	for flips in xrange(cutoff):
		try:
			#print(''.join(['-+'[s] for s in stove]))
			x = stove.index(False)
		except ValueError:
			return flips
		else:
			flip(stove, x, k)
	else:
		raise RuntimeError

#while True:
	#n = random.randint(2, 1000)
	#k = random.randint(2, n)
	#stove, flips = generate(n, k)
	#print(n, k, ltr(stove, k, flips), flips)

T = int(raw_input())
for case in xrange(T):
	S, K = raw_input().split()
	S = [s == '+' for s in S]
	K = int(K)
	try:
		soln = ltr(S, K, 999999999)
	except IndexError:
		print "Case #%s: IMPOSSIBLE" % (case+1)
	else:
		print "Case #%s: %s" % (case+1, soln)