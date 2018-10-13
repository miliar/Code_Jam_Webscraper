import sys

filename = sys.argv[1]

fd = open(filename, 'r')
op = open('output.dat', 'w')
flag = 0
count = 0


def int2bin(n, count=24):
	return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

for line in fd:
	if flag == 0:
		flag = 1
		continue
	else:
		count += 1
	var = line.split()
	n = int(var[0])
	k = int(var[1])
	kbin = "".join(['1']*n)
	nbin = int2bin(k, n)	
	if nbin == kbin:
		op.write("Case #" + str(count) + ": ON")
		op.write('\n')		 
	else:
		op.write("Case #" + str(count) + ": OFF")
		op.write('\n')
		

	
