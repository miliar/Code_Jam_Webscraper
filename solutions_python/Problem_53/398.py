from numpy import *

#lines = open("a_test1.in").read().split("\n")
#lines = open("A-small-attempt0.in").read().split("\n")
#lines = open("A-small-attempt1.in").read().split("\n")
#lines = open("A-small-attempt2.in").read().split("\n")
#lines = open("A-small-attempt3.in").read().split("\n")
lines = open("A-large.in").read().split("\n")

T = int(lines[0])
#print T 
output = []
for i in xrange(1, T+1):
	a = lines[i].split()
	n, k = int(a[0]), int(a[1])
	if k % 2**n == 2**n-1:
		state = 'ON' 
	else:
		state = 'OFF'
		
	output.append( 'Case #'+str(i)+': '+state )
	print i, ':', state, n, k

open("a.out", "w").write("\n".join(output))
#print "\n".join(output)