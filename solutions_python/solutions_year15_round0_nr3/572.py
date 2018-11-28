def readin(fname):
	with open(fname, 'r') as f:
		contents = f.readlines()
	ntrials = int(contents[0])
	trials = [contents[2*i+1].replace('\n', '').split(' ') + [contents[2*i+2].replace('\n','')] for i in range(0, ntrials)]
	trials = [[int(a[0]), int(a[1]), a[2]] for a in trials]
	return [ntrials, trials]

multmap = {
	'11': '1',
	'1i': 'i',
	'1j': 'j',
	'1k': 'k',
	'i1': 'i',
	'ii': '2',
	'ij': 'k',
	'ik': 'J',
	'j1': 'j',
	'ji': 'K',
	'jj': '2',
	'jk': 'i',
	'k1': 'k',
	'ki': 'j',
	'kj': 'I',
	'kk': '2',
}

reverse = {
	'1': '2',
	'i': 'I',
	'j': 'J',
	'k': 'K',
	'2': '1',
	'I': 'i',
	'J': 'j',
	'K': 'k',
}

toi = []
toj = []
tok = []

def buildmultmap():
	# Build multiplication map
	for k, v in list(multmap.items()):
		multmap[reverse[k[0]] + k[1]] = reverse[v]
		multmap[k[0] + reverse[k[1]]] = reverse[v]
		multmap[reverse[k[0]] + reverse[k[1]]] = v

dynamic = {}

def evaluate(partition):
	if partition in dynamic:
		return dynamic[partition]
	if len(partition) == 1:
		return partition
	if len(partition) == 2:
		return multmap[partition]
	sol = multmap[evaluate(partition[:len(partition)/2]) + evaluate(partition[len(partition)/2:])]
	dynamic[partition] = sol
	return sol

def solve(trial):
	L = trial[0]
	X = trial[1]
	T = X * L
	s = trial[2] * X
	if evaluate(s) != '2':
		return 'NO'
	for i in range(1,len(s)-1):
		if evaluate(s[:i]) == 'i':
			for j in range(i+1, len(s)):
				if evaluate(s[i:j]) == 'j' and evaluate(s[j:]) == 'k':
					return 'YES'
	return 'NO'

def main():
	buildmultmap()
	[ntrials, trials] = readin('C-small-attempt1.in')
	f = open('answer.out', 'w')
	for i in range(0,ntrials):
		solution = solve(trials[i])
		print i, solution
		f.write('Case #%d: %s\n' % (i+1, solution))
	f.close()

if __name__=='__main__':
	main()