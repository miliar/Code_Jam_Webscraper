import sys
import fileinput

def isrecycled(x,y):
	xs = str(x)
	ys = str(y)
	for i in xrange(1,len(ys)): # don't do all of ys
		if ys[i:] + ys[:i] == xs:
			return True
	return False

# calls isrecycled (a-b)*((a-b)+1)/2 times
def numrecycled_bruteforce(a,b):
	count = 0
	for i in xrange(a,b+1):
		for j in xrange(i+1,b+1):
			if isrecycled(i,j):
				count += 1
	return count

# loops (a-b)*length*numpairs times, uses memory equal to number of possible pairs
def numrecycled_generate(a,b):
	length = len(str(a))

	# yields for each recyclable pair that can be constructed out of x (excluding itself)
	def pairs(x):
		xs = str(x)
		ps = []
		for count in xrange(1,length):
			pair = xs[count:] + xs[:count]
			if (pair[0] != '0'):
				ipair = int(pair)
				if (ipair != x) and (ipair <= b) and (ipair > x):
					yield (x,int(pair))

	# For every number, generate all of its recycled pairs.
	allpairs = set()
	for i in xrange(a,b+1):
		for p in pairs(i):
			allpairs.add(p)
		
	# count the number of distinct pairs
	return len(allpairs) 

count = 0
for line in fileinput.input():
	if fileinput.isfirstline():
		continue

	a,b = map(int,line.split())
	answer=numrecycled_generate(a,b)

	count += 1
	print("Case #{}: {}".format(count,answer))
