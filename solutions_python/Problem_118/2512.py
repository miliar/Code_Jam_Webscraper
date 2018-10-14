import math
t = int( raw_input() )

def is_pan( x):
	for i in range(len(x)):
		if x[i] != x[len(x)-i-1]:
			return False
	return True

for i in range(t):
	a, b = map( int, raw_input().split(' '))
	cnt = 0
	for num in range( a, b+1):
		data = str(num)
		if not is_pan( data):
			continue
		_sqrt = int(math.sqrt(num))
		if _sqrt * _sqrt == num:
# print data,
			data = str(_sqrt)
			if is_pan( data):
				cnt += 1
#print num
# print data
	print "Case #{0}: {1}".format( i+1, cnt)
