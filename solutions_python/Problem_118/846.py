from itertools import product

def palindromeNum(n):
   return [n*'%s'%tuple(list(i)+list(i[n*(n-1)/2%(n-1)-1::-1])) for i in product(*([range(1,10)]+[range(0,10)]*((n+1)/2-1)))]
#n>1
print '\n'.join([str(x) for x in xrange(1,10)])
for n in xrange(1,input()):
	print '\n'.join(palindromeNum(n+1))