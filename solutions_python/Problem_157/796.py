table = [['1','i','j','k'],
		 ['i','-1','k','-j'],
		 ['j','-k','-1','i'],
		 ['k','j','-i','-1']]

index = {'1': 0,
		 'i': 1,
		 'j': 2,
		 'k': 3}

def multiply(x, y):
	minus = 1
	if(x[0]=='-'):
		minus *= -1
		x = x[1:]
	if(y[0]=='-'):
		minus *= -1
		y = y[1:]
	tabval =table[index[x]][index[y]]
	if(tabval[0]=='-'):
		minus *= -1
		tabval = tabval[1:]
	if(minus == -1):
		moins = '-'
	else:
		moins = ''
	res= moins + tabval
	return (res)

def simplify(string):
	return reduce(lambda x,y: multiply(x, y), list(string), '1')

def solve(string, occu):
	built_string  = [string for i in range(occu)]
	built_string = list(reduce(lambda x,y: x+y,built_string))
	s = len(built_string)
	for i in range(s):
		debut = built_string[0:i]
		print debut
		if(simplify(debut) == 'i'):
			for j in range(i, s):
				milieu = built_string[i:j]
				if(simplify(milieu) == 'j'):
					if (simplify(built_string[j:]) == 'k'):
						return 'YES'
	return 'NO'

def solve2(string, occu):
	string  = [string for i in range(occu)]
	string = list(reduce(lambda x,y: x+y,string))
	m = len(string)
	kind= [];
	prefix = [];
	ival = '1'
	kval = '1'
	for i in range(m):
		ival = multiply(ival, string[i])
		prefix.append(ival)
		kval = multiply(string[m-i-1], kval)
		if(kval == 'k'):
			kind.append(m-i-1);
	nb_k = len(kval)
	# print prefix, kind
	for cur_k_ind in kind:
		if (prefix[cur_k_ind-1] == 'k'):
			if('i' in prefix[:cur_k_ind]):
				return 'YES'
	return 'NO'
#print(simplify('iji'))

#print solve2('jijijijijiji', 1)

def parse_cases(filename):
	fhandle = open(filename)
	lines = fhandle.readlines()
	curline = 0
	nb_cases = int(lines[curline])
	curline +=1
	finished = False
	outfile = open("outfile.out", 'w')
	while(not(curline>=2*nb_cases+1)):
		lx = map(int , lines[curline].split())
		x = lx[1]
		curline+=1
		string = lines[curline].split()[0]
		curline+=1
		solution = solve2(string, x)
		print "Case #%d: %s" %(curline/2, solution)
		outfile.write("Case #%d: %s\n" %(curline/2, solution))
	fhandle.close
	outfile.close

parse_cases('C-small-attempt1.in')