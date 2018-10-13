import sys

f = open(sys.argv[1])
f.readline()
casenum = 1

l = f.readline()
while l != "":
	a,b,k = [int(x) for x in l.split()]
	output = 0

	for x in range(a):
		for y in range(b):
			if x&y < k:
				output += 1

	print "Case #{}: {}".format(casenum,output)
	l = f.readline()
	casenum += 1
f.close()