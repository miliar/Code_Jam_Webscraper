import time
import itertools

def check(string):
	# print string
	ch = [c for c in string]
	return ( ch == ch[::-1] )

f = open("in.txt")
T = int(f.readline())
bag = ['0','1','2']

for case in range( T ):
	start = int(time.time())
	
	ans = 0
	A,B = (int(x) for x in f.readline().split())
	lowLength = len( str(int(A**0.5)) )
	highLength = len( str(int(B**0.5)) )

	if lowLength < 2: lowLength = 2

	for length in range(lowLength, highLength+1):
		# print "length:", length
		combo = itertools.product( bag, repeat=length)
		# print "length of combo", len( list(combo) )
		for tup in combo:
			strNum = ''.join( c for c in tup)
			num = int( str(strNum) )
			if len(str(num)) < length: continue
			else:
				sqrNum = num ** 2
				if A <= sqrNum and sqrNum <= B:
					ans += check( str(sqrNum) )

	for specialCase in [1,4,9]:
		if A <= specialCase and B >= specialCase: ans += 1
	
	
	print "Case #{}: {}".format( case+1, ans )

	# print int(time.time()) - start