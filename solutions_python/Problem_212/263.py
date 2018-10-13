import math

def solve(  ):
	n, p = [int(x) for x in input().split() ]
	remain = [0 for x in range(p)]
	for g in [int(x) for x in input().split()]:
		remain[g % p] += 1
	divisible = remain[0]
	remain [0] = 0
	if p==2:
		uber = remain[1]//2
		divisible += uber
		remain[1] -= uber*2
		
	if p==3:
		uber = min( remain[1], remain[2] )
		divisible += uber
		remain[1] -= uber
		remain[2] -= uber
		
		uber = remain[1] //3
		divisible += uber
		remain[1] -= 3*uber
		
		uber = remain[2] //3
		divisible += uber
		remain[2] -= 3*uber
		
	if p ==4:
		uber = remain[2]//2
		divisible += uber
		remain[2] -= uber*2
		
		uber = min(remain[1], remain[3])
		divisible += uber
		remain[1] -= uber
		remain[3] -= uber
		
		uber = remain[1] //4
		divisible += uber
		remain[1] -= uber *4
		
		uber = remain[3] //4
		divisible += uber
		remain[3] -= uber * 4
	if sum(remain) == 0:
		return divisible
	else: 
		return divisible +1
	

t = int( input() )

for testcase in range (1,t+1):
	print ("Case #{0}: {1}" .format(testcase, solve(  ) ) )
	
	