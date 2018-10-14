import sys

try: 
	f = open(sys.argv[1])
	out = open(sys.argv[1].rpartition("\\")[2]+".out", 'w')

	numTests = int(f.readline())

	for i in range (0, numTests):
		#a1 = int(f.readline())
		vals = f.readline()[0:-1].split(" ")
		
		shyness = []
		
		Smax = int(vals[0])
		for j in range(0,Smax+1):
			shyness.append(int(vals[1][j]))
		#	print "shyness" + str(j) +": " + str(shyness[j])
			
		invite = 0
		standing = 0
		
		for k in range(0,Smax+1):
			if k <= standing:
				standing+= shyness[k]
			#	print str(k) + " not shy " + str(standing) + " standing"
			else:
				newinvite = k-standing
				invite += newinvite
				standing += newinvite
				standing += shyness[k]
			#	print str(k) + " shy, inviting " + str(newinvite)
		

		out.write("Case #" + str(i+1) +": " + str(invite) + "\n")


except IOError, e:
	print "Error %d: %s"%(e.args[0], e.args[1])

