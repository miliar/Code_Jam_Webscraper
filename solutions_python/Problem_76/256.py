import itertools
from operator import xor

def patrick_add(a,b):
	return a^b
	
assert(1==patrick_add(5,4))
assert(14==patrick_add(7,9))
assert(3==reduce(xor,[5,6]))
assert(1==reduce(xor,[5,4]))


def copy_list(list_in):
	cop = []
	for thing in list_in:
		cop.append(thing)
	return cop

f = open('candyinput.txt','r')
trials = int(f.readline())
for i in xrange(1,trials+1):
	#print "trial %d"%i
	num_candies = int(f.readline())
	values = map(long,f.readline().split())
	values.sort()
	max_val = -1
	for candy_num in xrange(num_candies-1,0,-1):
		for perm in itertools.combinations(values,candy_num):
			opposite = []
			opposite = copy_list(values)
			for p in perm:
				opposite.remove(p)
			pats = reduce(xor,perm)
			if(pats == reduce(xor,opposite)):
				actual_pats = sum(perm)
				if(actual_pats > max_val):
					max_val = actual_pats 
	#print "We have {0} candies with values {1}".format(num_candies,values)
	if(max_val > 0):
		print "Case #{0}: {1}".format(i,max_val)
	else:
		print "Case #{0}: NO".format(i)
	
	
	