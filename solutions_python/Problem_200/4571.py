import sys
 
lines = iter(sys.stdin.read().splitlines())
 
T = int(next(lines))
 
for i in range(T):
	
	N = [ int(digit) for digit in next(lines) ]
	
	for pos in reversed(range(1,len(N))):
		if N[pos-1] > N[pos]:
			for rest in range(pos,len(N)):
				N[rest] = 9
			N[pos-1] += -1
	
	R = int( ''.join(str(digit) for digit in N) )
	
	print( 'Case #', i+1, ': ', R, sep = '' )