import itertools

usableSums = [0, 1, 4];

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
	
def rep(s, m):
    a, b = divmod(m, len(s))
    return s * a + s[:b]

def sumSqrDigs(x):
	sum = 0
	for dig in x:
		val = int(dig)
		sum += val*val

	return sum
	
def makePalindrome(x, middle=''):
	return x + middle + x[::-1]
	
def possiblePalindromes(x):
	global usableSums
	
	sum = sumSqrDigs(x) * 2
	if sum < 10:
		yield makePalindrome(x, '')
		for i, n in enumerate(usableSums):
			if sum+n <= 10:
				yield makePalindrome(x, str(i))
			else:
				break

def countInRange(low, high):
	count = 0
	if low <= 1 and high >= 1:
		count += 1
	if low <= 4 and high >= 4:
		count += 1
	if low <= 9 and high >= 9:
		count += 1
	for ones in range(1,5):
		for zeros in range(25):
			for dig in range(1, 3):
				toTest = str(dig)*ones + '0'*zeros
				m = makePalindrome(toTest)
				if int(m)*int(m) > high:
					continue
				for perm in perm_unique([c for c in toTest]):
					if perm[0] is not '0':
						for pal in possiblePalindromes(''.join(str(c) for c in perm)):
							squared = int(pal)*int(pal)
							if squared <= high and squared >= low:
								count += 1

	return count
	
fr = open("C-small-attempt.in", 'r')
fw = open("output.txt", 'w')
lines = [line for line in fr]

numTests = 0

for i, line in enumerate(lines):
	if i == 0:
		numTests = int(line)
	else:
		test = [a.replace('\n','') for a in line.split(' ')]
		fw.write("Case #%d: %s\n" % (i, countInRange(int(test[0]), int(test[1]))))
	
fr.close()
fw.close()
#print countInRange(100,1000)