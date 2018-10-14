f = open('a.s', 'r');
f2 = open('a.out', 'w');

tests = f.readline()

array1 = [[0 for x in xrange(4)] for x in xrange(4)] 
array2 = [[0 for x in xrange(4)] for x in xrange(4)] 

msg = 'Case #{0}: {1}\n'

for i in range(int(tests)):
	row1 = int(f.readline())
	array1[0] = [int(x) for x in f.readline().split()]
	array1[1] = [int(x) for x in f.readline().split()]
	array1[2] = [int(x) for x in f.readline().split()]
	array1[3] = [int(x) for x in f.readline().split()]
	
	row2 = int(f.readline())
	array2[0] = [int(x) for x in f.readline().split()]
	array2[1] = [int(x) for x in f.readline().split()]
	array2[2] = [int(x) for x in f.readline().split()]
	array2[3] = [int(x) for x in f.readline().split()]
	
	c = list(set(array1[row1-1]).intersection(array2[row2-1]))
	
	length = len(c)
	out = ''
	
	if length == 1:
		out = c[0]
	elif length > 1:
		out = 'Bad magician!'
	else:
		out = 'Volunteer cheated!'
		
	f2.write( msg.format((i+1), out))

	#with open('file') as f:
    #w, h = [int(x) for x in f.readline().split()]
    #array = [[int(x) for x in line.split()] for line in f]