import sys

filename = sys.argv[1]

from fractions import gcd
fd = open(filename, 'r')
op = open('output.dat', 'w')
flag = 0
count = 0

for line in fd:
	if flag == 0:
		flag = 1
		continue
	else:
		count += 1
		years = line.split()		
		ycount = int(years[0])
		years = [int(x) for x in years[1:]]
		years.sort()		
		if ycount > 2:
			div = gcd(years[1] - years[0], years[2] - years[1])
		else:
			div = max(years) - min(years)
		#print div
		i = 1
		pro = 1
		while( pro < years[0]):
			pro = div * i
			i += 1
		op.write("Case #" + str(count) + ": " + str(pro - years[0]))
		op.write('\n')	
		
