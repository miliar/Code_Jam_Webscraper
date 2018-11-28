from time import time

def nextCase():
	fileName = "D-small-attempt2.in"
	T = None
	N = None
	for line in open(fileName, 'r').readlines():
		if None == T: T = int(line)
		elif None == N: 
			K, N = tuple([int(x) for x in line.split(' ')])
			i = 0
			startKeys = None
			chests = [None for i in range(N)]
		elif None == startKeys: 
			startKeys = [int(x) for x in line.split(' ')]
		else:
			d = [int(x) for x in line.split(' ')]
			chests[i] = [d[0], d[2:]]
			i += 1
			if N == i: 
				N = None
				yield startKeys, chests

def keys(K):
	r = {i: 0 for i in range(1, 401)}

	for k in K: r[k] += 1

	return r

def addKeys(K, K1):
	for k in K1: K[k] += 1
	return K

def removeKeys(K, K1):
	for k in K1: K[k] -= 1
	return K

def solve(T):
	K = keys(T[0])
	chests = [[False] + T[1][i] for i in range(len(T[1]))]

	cache = dict()
	def engine(mask, level):
		if mask in cache: return cache[mask]
		if level == len(chests): return True, ""
		
		r, chain = False, ""
		for i in range(len(chests)):
			if not chests[i][0] and (K[chests[i][1]] > 0):#not opened yet
				chests[i][0] = True
				removeKeys(K, [chests[i][1]])
				addKeys(K, chests[i][2])
				r, chain = engine(mask | (1 << i), level + 1)
				chests[i][0] = False
				removeKeys(K, chests[i][2])
				addKeys(K, [chests[i][1]])
				if r: 
					chain = str(i + 1) + (" " if "" != chain else "") + chain
					break

		cache[mask] = (r, chain)
		return r, chain
				
	r, chain = engine(0, 0)
	return chain if r else "IMPOSSIBLE"

start = time()

i = 1
for T in nextCase():
	print("Case #%d: %s" % (i, solve(T)))
	i += 1


#print(time() - start)
