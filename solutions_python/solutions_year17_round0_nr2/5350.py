import operator
import itertools
import sys
def is_sorted(collection, pred=operator.lt):
		length=len(collection)
		if length < 2:
			return True

		for i in xrange(length - 1):
			if pred(collection[i+1], collection[i]):
				return False
		return True

for _ in xrange(int(raw_input())):
	no=raw_input()
	a=list(no)
	b=int(no)
	lol=map(int,a)
	flag=1
	while(flag==1):
		if is_sorted(lol):
			flag=0
		else:
			b=b-1
			#print b
			a=list(str(b))
			lol=map(int,a)

	print "Case #"+repr(_+1)+": "+repr(b)