import fractions
import sys
import math
c = int(sys.stdin.readline())
for i in range(0,c):
	line = sys.stdin.readline().split()
	n = int(line[0])
	result = math.fabs(int(line[1])-int(line[2]))
	m = int(line[1])
	for j in range(2,n+1):
		m = min(m,int(line[j]))
	for j in range(1,n):
		for k in range(j+1,n+1):
			result = fractions.gcd(result,math.fabs(int(line[j])-int(line[k])))
	print 'Case #'+str(i+1)+': ',
	if m%int(result)==0:
		print 0
	else:
		print (int(m)/int(result)+1)*int(result)-int(m)
