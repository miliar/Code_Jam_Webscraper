def solve(in_name, out_name):
	fin = open(in_name, 'r');
	L = [map(int, x.strip().split()) for x in fin.readlines()]
	fin.close()
	T = L[0][0];
	outlines = [];
	
	k = 1
	for i in xrange(T):
		x1 = L[k][0]
		r1 = L[k+x1]
		k += 5
		x2 = L[k][0]
		r2 = L[k+x2]
		k += 5
		common = list(set(r1).intersection(set(r2)))
		curelt = 'Case #' + str(i+1) + ': ';
		
		if(len(common)==0):
			curelt += 'Volunteer cheated!'
		elif len(common)>1:
			curelt += 'Bad magician!'
		else:
			curelt += str(common[0])
		
		curelt += '\n'
		outlines.append(curelt)
		
	fout = open(out_name, 'w')
	fout.writelines(outlines)
	return
	
solve('A-small-attempt0.in', 'A-small-attempt0.out')

#solve('A-test.in', 'A-test.out')
