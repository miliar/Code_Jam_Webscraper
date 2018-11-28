import sys

inpath = sys.argv[1]
outpath = sys.argv[2]

multiplication = {'1': {'1': '1', 'i': 'i' , 'j': 'j' , 'k': 'k'},
		  'i': {'1': 'i', 'i': '-1', 'j': 'k' , 'k': '-j'},
		  'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'},
		  'k': {'1': 'k', 'i': 'j' , 'j': '-i', 'k': '-1'}}

def multiply(s1, s2):
	"""
	simple multiplication function using a dictionary
	negative values are checked but are not included in the
	dictionary multiplication table
	"""
	negative = False
	if s1[0] == '-':
		negative = not negative
		s1 = s1[1:]
	if s2[0] == '-':
		negative = not negative
		s2 = s2[1:]
	result = multiplication[s1][s2]
	# need to check if result is negative as well
	# otherwise we could return two '-' signs
	if result[0] == '-':
		negative = not negative
		result = result[1:]
	return ('-' if negative else '') + result

infile = open(inpath, "r")
outfile = open(outpath, "w")
tests = int(infile.readline())
for testNr in range(tests):
	possible = False
	L, X = map(int, infile.readline().split())
	s = infile.readline()[:-1]
	assert(len(s) == L)
	s = "".join([s for _ in range(X)])
	negative = False

	# loop until first character is 'i'
	i,j,k = '1','1','1'
	index = 0

	# find out when first letter becomes 'i'
	while i != 'i' and index < L*X:
		i = multiply(i, s[index])
		index += 1
	
	# find out when second letter becomes 'j'
	while j != 'j' and index < L*X:
		j = multiply(j, s[index])
		index += 1

	# calculate what third letter is
	while index < L*X:
		k = multiply(k, s[index])
		index += 1

	result = i + j + k
	outfile.write("Case #{}: {}\n".format(testNr+1, "YES" if result == 'ijk' else "NO"))
outfile.close()
infile.close()
