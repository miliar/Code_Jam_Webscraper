#!/usr/bin/python

import sys

# Memoization pattern
class basic_mem:
	def __init__ (self, function):
		self.function = function
		self.cache = {}	
	
	def __call__ (self, *args, **kwargs):
		key = str(args) + str(kwargs)
		if key in self.cache:
			return self.cache[key]
		else:
			result = self.function(*args, **kwargs)
			self.cache[key] = result
			return result

# How Patrick thinks...
def patricksum (candies):
	return reduce(lambda x,y:x^y, candies)

# How Sean thinks
def seansum (L):
	return reduce (lambda x,y:x+y, L)

# A function to allow ordering lists of lists (with my particular order)
def valueofset (L):
	v = seansum (L)
	a = (1 - 1./len(L))
	
	for i in xrange(0, len(L)):
		a += (1.-a)/L[i]
	v += a
	
	return v

# Returns the "minimum" list (with my particular order)
def minset (L):
	min (L, key = valueofset )

# Returns "L1 - L2"
def complist (L1, L2):
	L = L1[:]
	for l in L2:
		L.remove(l)
	return L

# Creates the list of partitons of the number n
@basic_mem
def partitions(n):
	if n == 1:
		return [[1]]
	
	partitionslist = []
	
	for k in range(n,0,-1):
		tail = partitions (n-k)
		
		for x in tail:
			partition = [k] + x
			partitionslist.append(partition)
	
	return partitionslist

# Tells us if l1 is sublist of l2
# (I can't work with the set class because repeated items)
def issublist(l1, l2):
	sublist = True
	
	for i in l1:
		if i not in l2:
			sublist = False
			break
	
	return sublist

def main ():
	args = sys.argv[1:]
	
	f = open(args[0])
	ncases = int(f.readline())
	
	for i in xrange(0, ncases):
		ncandies = int(f.readline())
		candies  = map(int, f.readline().rsplit())
		candies.sort()
		
		if patricksum (candies) != 0:
			r = "NO"
		else:
			patrick = candies[:1]
			sean = candies[1:]
			
			while patricksum (patrick) != patricksum (sean):
				
				k = seansum (patrick)
				potentialsets = filter (lambda p: issublist(p, candies), partitions(k))
				
				patrick = minset (
					filter (
						lambda x:
							valueofset2(x) > valueofset2(patrick),
						potentialsets
					)
				)
				
				sean = complist (candies, patrick)
			r = seansum (sean)
		
		print "Case #"+str(i+1)+":", r

if __name__ == "__main__":
	main ()
	
