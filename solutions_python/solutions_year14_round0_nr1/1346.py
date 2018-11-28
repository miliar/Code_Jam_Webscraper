fileinput = open("A-small-attempt0.in")

T = int(fileinput.readline().strip())

for i in range(T):
	set1 = set();
	set2 = set();

	x = int(fileinput.readline().strip())
	#print "First row is {}".format(x)
	for j in range(4):
		if(j == x-1):
			set1 = set(fileinput.readline().strip().split())
		else:
			fileinput.readline()


	x = int(fileinput.readline().strip())
	#print "second row is {}".format(x)
	for j in range(4):
		if(j == x-1):
			set2 = set(fileinput.readline().strip().split())
		else:
			fileinput.readline()

	#print set1, set2
	set3 = set1.intersection(set2)

	if(len(set3) == 0):
		print "Case #{}: Volunteer cheated!".format(i+1)
		continue
	if(len(set3) > 1):
		print "Case #{}: Bad magician!".format(i+1)
		continue
	else:		
		print "Case #{}: {}".format(i+1, list(set3)[0])
		continue



		
