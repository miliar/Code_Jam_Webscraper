import sys
file = sys.argv[1]
input = open(file,'r')
i = 0
t = int(input.readline())
# there are t cases bt we will loop till end of file

for line in input.readlines():
	result = "ON"
	i = i+1
	nk = line.split()
	n = int(nk[0])
	k = int(nk[1])
	if ((k+1)%(2**n))!=0:
		result = "OFF"
	print "Case #"+str(i)+": "+ result
input.close()


