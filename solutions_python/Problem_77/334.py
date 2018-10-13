import sys

filename = sys.argv[1]
f = open(filename, 'r')

for i in range(int(f.readline().strip())):
	f.readline()
	list = f.readline().strip().split()
	result = 0
	for l in list:
		if int(l) != list.index(l)+1:
			result+=1
	print 'Case #'+str(i+1)+':', result