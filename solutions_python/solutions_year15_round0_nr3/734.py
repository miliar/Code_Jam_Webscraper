inputFile = open('C-small-attempt0.in', 'r')
inString = inputFile.read()
inputLines = inString.split('\n')
inputLines.pop(0)
inputLines.pop()
output = ''
case = 1

products = {
	'11' : '1',
	'1i' : 'i',
	'1j' : 'j',
	'1k' : 'k',
	'i1' : 'i',
	'ii' : '-1',
	'ij' : 'k',
	'ik' : '-j',
	'j1'  : 'j',
	'ji' : '-k',
	'jj' : '-1',
	'jk' : 'i',
	'k1' : 'k',
	'ki' : 'j',
	'kj' : '-i',
	'kk' : '-1'
};

def product(m1, m2):
	isNegative = False
	m0 = m1
	if '-' in m1:
		isNegative = True
		m1 = m1[1:]
	rtnProduct = products[str(m1 + m2)]
	if isNegative: 
		if '-' in rtnProduct:
			rtnProduct = rtnProduct[1:]
		else: 
			rtnProduct = '-' + rtnProduct
	return rtnProduct

lineNumber = 1
mulitplier = 1
for line in inputLines:
	if lineNumber  % 2 == 1:
		multiplier = int(line.split(' ')[1])
	else:	
		i = False
		j = False
		k = False
		characterGroup = list(line)
		characterGroup = characterGroup * multiplier
		currentProduct = '1'
		trailingProduct = '1'
		for character in characterGroup:
			currentProduct = product(currentProduct, character)
			if i == False:
				if currentProduct == 'i':
					i = True
					currentProduct = '1'
			elif j == False:
				if currentProduct == 'j':
					j = True
					currentProduct = '1'
			elif k == False:
				if currentProduct == 'k':
					k = True
					currentProduct = '1'
			else:
				trailingProduct = currentProduct
		result = 'YES' if i and j and k and trailingProduct == '1' else 'NO'
		output += ('Case #' + str(case) + ': ' + result + '\n')
		case += 1
	lineNumber += 1

outputFile = open('out1.out', 'w')
outputFile.write(output)