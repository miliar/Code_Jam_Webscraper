# http://stackoverflow.com/questions/6284396/permutations-with-unique-values
class unique_element:
    def __init__(self,value,occurrences):
        self.value = value
        self.occurrences = occurrences

def perm_unique(elements):
    eset=set(elements)
    listunique = [unique_element(i,elements.count(i)) for i in eset]
    u=len(elements)
    return perm_unique_helper(listunique,[0]*u,u-1)

def perm_unique_helper(listunique,result_list,d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d]=i.value
                i.occurrences-=1
                for g in  perm_unique_helper(listunique,result_list,d-1):
                    yield g
                i.occurrences+=1

# my

def ispal(x):
	if not type(x) == str:
		x = str(x)

	return x == x[::-1]

def makepal(x, evenlen=False):
	t = type(x)
	if t != str:
		x = str(x)
	if evenlen:
		ret = x + x[::-1]
	else:
		ret = x[:-1] + x[::-1]
	ret = t(ret)
	return ret

def makepali(x, evenlen=False):
	return int(makepal(x, evenlen))

def fair(x):
	"""fair, <= x"""
	"""
1, 2, 3

I. With '2':

1. 1 x '2':  1 ? 2 ? 1
a) sqrsum = 6
1 0* 2 0* 1
b) sqrsum = 8
1 0* 1 0* 2 0* 1 0* 1

2. 2 x '2'
2. a) 2 0* 2
2. b) 2 0* 1 0* 2

II. Only '1':

1. 2 | len
sqrsums: 2, 4, 6, 8

2. not 2 | len
sqrsums: 2-9
a) middle 0
sqrsums 2, 4, 6, 8

b) middle 1
sqrsums 3, 5, 7, 9



"""
	if x < 0:
		return 0
	small = 1
	if x >= 1:
		small += 1
	if x >= 4:
		small += 1
	if x >= 9:
		small += 1
	# I. 1. a)
	I1a = 0
	zeros = ''
	while makepali('1' + zeros + '2') ** 2 <= x:
		I1a += 1
		zeros += '0'
	#print 'I. 1. a)\t', I1a

	# I. 1. b)
	I1b = 0
	zeros = ''
	while makepali('1' + zeros + '12') ** 2 <= x:
		middle = zeros + '1'
		for i in perm_unique(middle):
			if makepali('1' + ''.join(i) + '2') ** 2 <= x:
				I1b += 1
		zeros += '0'
	#print 'I. 1. b)\t', I1b

	# I. 2. a)
	I2a = 0
	zeros = ''
	while int('2' + zeros + '2') ** 2 <= x:
		I2a += 1
		zeros += '0'
	#print 'I. 2. a)\t', I2a

	# I. 2. b)
	I2b = 0
	zeros = ''
	while makepali('2' + zeros + '1') ** 2 <= x:
		I2b += 1
		zeros += '0'
	#print 'I. 2. b)\t', I2b

	# II. 1.
	II1 = 0
	for ones in ('', '1', '11', '111'):
		zeros = ''
		middle = zeros + ones
		while makepali('1' + zeros + ones, True) ** 2 <= x:
			for i in perm_unique(middle):
				if makepali('1' + zeros + ones, True) ** 2 <= x:
					II1 += 1
			zeros += '0'
			middle = zeros + ones
	#print 'II. 1.\t\t', II1

	# II. 2. a)
	II2a = 0
	for ones in ('', '1', '11', '111'):
		zeros = ''
		middle = zeros + ones
		while makepali('1' + zeros + ones + '0') ** 2 <= x:
			for i in perm_unique(middle):
				if makepali('1' + zeros + ones + '0') ** 2 <= x:
					II2a += 1
			zeros += '0'
			middle = zeros + ones
	#print 'II. 2. a)\t', II2a

	II2b = 0
	for ones in ('', '1', '11', '111'):
		zeros = ''
		middle = zeros + ones
		while makepali('1' + zeros + ones + '1') ** 2 <= x:
			for i in perm_unique(middle):
				if makepali('1' + zeros + ones + '1') ** 2 <= x:
					II2b += 1
			zeros += '0'
			middle = zeros + ones
	#print 'II. 2. b)\t', II2b

	return I1a + I1b + I2a + I2b + II1 + II2a + II2b + small


tst = int(raw_input())
for i in range(0,tst):
	f, t = raw_input().split(' ')
	print ''.join(['Case #', str(i + 1), ': ', str(fair(int(t)) - fair(int(f)-1))])
