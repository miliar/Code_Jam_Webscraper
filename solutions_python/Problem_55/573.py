import sys
# open input file
file = sys.argv[1]
input = open(file,'r')
t = int(input.readline())

# there are t cases...
for i in range(0, t):
	#  parse data for each cases
	firstline = input.readline()
	rkn=firstline.split()
	r = int(rkn[0])
	k = int(rkn[1])
	n = int(rkn[2])
	secondline = input.readline()
	g = secondline.split()
	# instances to keep track of money.
	m = 0

	# the roller coaster runs r times
	for j in range(0, r):
		count = 0
		if n == 1:
			m = m + int(g[0])
		else:
			first = 0;
			for l in range(0,n):
				temp = count + int(g[l])
				if (temp <= k):
					count = temp
					first = l+1
				else:
					first = l
					break
			gg = g[:]
			for o in range(0, n):
				index = o + first
				if index >= n-1:
					g[o] = gg[index-n]
				else:
					g[o] =gg[index]
			#print g
			m = m + count
	# coaster ran its max for one day
	print "Case #" + str(i+1) + ": " + str(m)
input.close()
