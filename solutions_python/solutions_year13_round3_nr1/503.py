def main():
	with open('A-small-attempt2.in', 'r') as f:
		line = f.readline()
		ncases = int(line)
		for i in xrange(1, ncases+1):
			line = f.readline()
			word, nlevel = line.split()
			nlevel = int(nlevel)
			solve(word, nlevel, i)

def solve(word, nlevel, case):
	nsubstr = 0
	for start in xrange(0, len(word)+1):
		for end in xrange(start+1, len(word)+1):
			if has_n_cons(word, start, end, nlevel):
				nsubstr += 1
	print "Case #%d: %d"% (case, nsubstr)


def has_n_cons(word, start, end, nlevel):
	# import pdb; pdb.set_trace()
	currentseq = 0
	maxseq = 0
	for char in  word[start:end]:
		if char not in ('a', 'e', 'i', 'o', 'u'):
			currentseq += 1
			if currentseq >= nlevel:
				return True
		else:
			currentseq = 0

	return False

main()