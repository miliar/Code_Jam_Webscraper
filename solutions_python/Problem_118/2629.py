import itertools

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def palindromes(k):
	return [sum([n*(10**i) for i,n in enumerate(([x]+list(ys)+[z]+list(ys)[::-1]+[x]) if k%2
	                                else ([x]+list(ys)+list(ys)[::-1]+[x]))])
	            for x in range(1,10)
	            for ys in itertools.permutations(range(10), k/2-1)
	            for z in (range(10) if k%2 else (None,))]

def calc():
	palin = range(10)
	for i in range(2, 17):
		palin += palindromes(i)
		print len(palin)

	max = 1125899906842620
	for i in xrange(len(palin)):
		if palin[i] > max:
			print i
			break

	palin = palin[:i]

	squarePals = []
	for pal in palin:
		if is_palindrome(pal**2):
			squarePals.append(pal**2)

	print squarePals

squarePals = [0, 1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10221412201, 12102420121, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121]
def solve(a, b):
	count = 0 
	for sp in squarePals:
		if (sp >= a and sp <= b):
			count += 1
	return count


lines = open('C-small-attempt0.in', 'r').readlines()[1:]
for i, line in enumerate(lines):
	numbers = set()
	print 'Case #' + str(i+1) + ': ' + str(solve(int(line.split()[0]), int(line.split()[1])))