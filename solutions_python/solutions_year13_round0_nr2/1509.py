def file_read(file):
	file_open = open(file, 'r')
	
	for line in file_open:
		yield line
	
	file_open.close()
	

input = file_read('B-small-attempt0.in')
output = open("B-small-attempt0.out","w")

T = int(input.next())

for k in xrange(T):

	a = []
	rows = []
	cols = []
	arr = input.next().split()
	N = int(arr[0])
	M = int(arr[1])
	
	for i in xrange(N):
		rows += [0]
	for j in xrange(M):
		cols += [0]
	
	for i in xrange(N):
		a += [[]]
		arr = input.next().split()
		for j in xrange(M):
			a[i] += [arr[j]]
			if rows[i] < arr[j]:
				rows[i] = arr[j]
			if cols[j] < arr[j]:
				cols[j] = arr[j]
	
	possible = 1
	for i in xrange(N):
		for j in xrange(M):
			if a[i][j] != rows[i] and a[i][j] != cols[j]:
				possible = 0
				break;
	
	if possible == 1:
		output.write("Case #"+str(k+1)+": YES\n")
	else:
		output.write("Case #"+str(k+1)+": NO\n")