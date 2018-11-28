f = open('x','r');

fOut = open('output.txt','w')

def getBitSum(value):
	tot = 0;
	x = 1;
	while value > 0:
		tot += x;
		x = x*2;
		value -= 1;
	
	return tot + 1;
	
x = 1
for line in f:

	N = int(line.split(" ")[0])
	K = int(line.split(" ")[1])

	#print "N: " + str(N)
	#print "K: " + str(K)
	#print "N^(K-1): " + str(N^(K-1))
	#print "2^(K-1) % N^(K-1) : " + str(2^(K-1) % N^(K))
	
	bitSum = getBitSum(N)
	
	#print 'bitSum: ' + str(bitSum)
	#print 'K: ' + str(K)
	#print 'K % bitSum: ' + str(K % bitSum )
	
	if(K % bitSum == bitSum -1 ):
		fOut.write('Case #' + str(x) + ': ON\n')
		#print 'Case #' + str(x) + ': ON';
	else:
		fOut.write('Case #' + str(x) + ': OFF\n')
		#print 'Case #' + str(x) + ': OFF';
	x += 1
	
fOut.close()
f.close()