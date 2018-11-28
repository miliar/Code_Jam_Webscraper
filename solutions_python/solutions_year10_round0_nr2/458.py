import sys

def gcd( x, y ):
	a = max(x,y)
	b = min(x,y)

	while b != 0:
		remainder = a%b
		a = b
		b = remainder
	
	return a

input = file( sys.argv[1] )

C = int(input.readline())

for case in range(C):
	
	line = map( int, input.readline().strip().split(" ") )
	#print line;
	runningGCD = abs(line[1]-line[2])
	for i in range(3,line[0]+1):
		runningGCD = gcd( runningGCD, abs(line[i]-line[i-1]) )
	
	if line[1] % runningGCD == 0:
		result = 0
	else:
		result = runningGCD - (line[1]%runningGCD)
	
	output = "Case #%d: %s" % ( case+1, result )
	print output