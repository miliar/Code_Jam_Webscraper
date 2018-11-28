
f = open('A-large.in', 'r')
fout = open('A-large-out.txt', 'w')

t = int(f.readline().strip())

for i in range(t):
	d, n = f.readline().strip().split()
	d = int(d)
	n = int(n)
	print d,n
	mintime = 0
	for horse in range(n):
		k, s = f.readline().strip().split()
		k = int(k)
		s = int(s)
		time = (d-k)/float(s)
		mintime = max(mintime, time)
	print("Case #%d: %f"%(i+1, d/mintime))
	fout.write("Case #%d: %f\n"%(i+1, d/mintime))