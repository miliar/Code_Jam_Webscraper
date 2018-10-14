input_file = "a.in"
infile = open(input_file)

lines = infile.readlines();
t = int( lines[0] )
lines = lines[1:]
for i in range(t):
	print "Case #" + str(i+1) + ": ",
	a1 = int( lines[( i * 10 ) ].rstrip() )
	a = lines[( i * 10 ) + a1 ].rstrip().split(' ')
	b1 = int( lines[( i * 10 ) + 5 ].rstrip() )
	b = lines[( i * 10 ) + 5 + b1 ].rstrip().split(' ') 
	count = 0 
	num = 0
	for j in a:
		if( j in b ):
			count +=1
			num = j
	if count == 1:
		print num
	elif count == 0:
		print "Volunteer cheated!"
	else:
		print "Bad magician!"

