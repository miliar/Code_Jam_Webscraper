fin = open('in.txt','r')
fout = open('out.txt','w')
count = int(fin.readline().strip())
for i in range(count):
	fin.readline()
	arr = fin.readline().strip().split(' ')
	n = 0.0
	for j in range(len(arr)):
		if j != int(arr[j])-1:
			n += 1
	fout.write( 'Case #%d: %f\n' % (i+1, n))
	