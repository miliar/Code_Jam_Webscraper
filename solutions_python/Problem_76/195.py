import sys
def f(i,first, second):
	s=[int(c) for c in second.split()]
	k = 0
	p = 0
	for j in s:
		k=k^j
	if k==0:
		result = sum(s) - min(s)
	else:
		result = "NO"

	print "Case #"+str(i)+": " + str(result)

b = open(sys.argv[1]).readlines()

for i in range(int(b[0])):
	f(i+1,b[i*2+1],b[i*2+2])


