def get_nr(S):
	invites, standing = 0, 0
	for i in xrange(len(S)):
		if standing < i:
			invites += (i-standing)
			standing = i
		standing += S[i]
	return invites

def solve(in_name, out_name):
	fin = open(in_name, 'rt');
	L = [map(int, x.strip().split()[1]) for x in fin.readlines()[1:]]
	fin.close()
	outlines = [];
	outlines = ["Case #" + str(i+1) + ": " + str(get_nr(L[i])) + '\n' for i in xrange(len(L))]
	fout = open(out_name, 'wt')
	fout.writelines(outlines)
	return

solve('A-large.in', 'A-large.out')	
#solve('A-small-attempt0.in', 'A-small-attempt0.out')

#solve('A-test.in', 'A-test.out')
