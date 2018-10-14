def solve_test_case(infile):
	N = int(infile.readline().rstrip())
	groups = []
	for i in xrange(N):
		groups.append(infile.readline().rstrip())
	wp = []
	for group in groups:
		games = len(group.replace('.',''))
		
		wp.append(float(group.count('1'))/games)

	wp_without_me = [] # without "me", list of lists
	for i in xrange(N):
		without_me = []
		for group in groups:

			newgroup = group[:i]+'.'+group[i+1:]

			games = len(newgroup.replace('.',''))
			without_me.append(float(newgroup.count('1'))/games)
		wp_without_me.append(without_me)
	
	opponents = [] # list of lists
	for group in groups:
		op_list = []
		for i, result in enumerate(group):
			if result != '.':
				op_list.append(i)
		opponents.append(op_list)
			
	
	owp = [sum(wp_without_me[i][g] for g in opponents[i])/len(opponents[i]) 
		   for i, group in enumerate(groups)]
	
	oowp = [sum(owp[g] for g in opponents[i])/len(opponents[i]) 
		    for i, group in enumerate(groups)]
	
	result = [0.25*wp[i]+0.5*owp[i]+0.25*oowp[i] for i in xrange(N)]
	
	#print 		
	return '\n'.join(str(r) for r in result)

def solve(filename):
	infile = open(filename, 'rb')
	T = infile.readline()
	for i in xrange(int(T)):
		result = solve_test_case(infile)
		print "Case #%d:" % (i+1)
		print result

if __name__ == "__main__":
	import sys
	solve(sys.argv[1])