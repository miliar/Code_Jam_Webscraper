f = open('B-large.in', 'r')
lines = f.readlines()

def function(C, F, X):
	F = float(F)
	a = 2
	time = 0
	while float(X)/float(a) > float(C)/float(a) + float(X)/float(a + F):
		time += float(C)/float(a)
		a += F
		#print (time, a, float(X)/float(a))
	return "%.7f" % (time + float(X)/float(a))



for i in xrange(int(lines[0])):
	input = lines[i+1].split()
	print "Case #%d: %s" %(i+1,function(input[0], input[1], input[2]))



#print function('30.0', '1.0', '2.0')
#print function(30.0, 2.0, 100.0)
#print function(30.50000, 3.14159, 1999.19990)
#print function(500.0, 4.0, 2000.0)