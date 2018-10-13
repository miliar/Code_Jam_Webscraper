f = open('C:\\Users\\narayv@amazon.com\\Desktop\\CodeJam\\A-small-attempt0.in', 'r')
output = open('C:\\Users\\narayv@amazon.com\\Desktop\\CodeJam\\output_a.txt', 'w')
N_O_T = int(f.readline())
i = 0 
#print N_O_T
#raw_input()

while i < N_O_T :
	#read test case
	f_answer = int(f.readline()) #First Answer
	
	#Read card arrangement - First Try
	j = 0
	arr1 = [] # arrangement 1

	# Read each line and store in the arrangement list (arr1)
	while j < 4:
		line = f.readline()
		if j == f_answer - 1:
			arr1 = [int(p) for p in line.split()]
		j = j +1
		
	s_answer = int(f.readline()) #Second Answer
	
	#Read card arrangement - Second Try
	k = 0
	arr2 = [] # arrangement 2

	# Read each line and store in the arrangement list (arr1)
	while k < 4:
		line = f.readline()
		if k == s_answer - 1 :
			arr2 = [int(p) for p in line.split()]
		k = k +1

	count = 0
	common = 0
	for f_item in arr1 :
		for s_item in arr2 :
			if f_item == s_item :
				count = count + 1
				common = s_item
	#Case #x: y
	if count == 1 :
		print "Case #" + str(i+1) + ": " + str(common)
		output.write("Case #" + str(i+1) + ": " + str(common) + "\n")
	elif count == 0:
		print "Case #" + str(i+1) + ": " + "Volunteer cheated!"
		output.write("Case #" + str(i+1) + ": " + "Volunteer cheated!\n")
	elif count > 1 :
		print "Case #" + str(i+1) + ": " + "Bad magician!"
		output.write("Case #" + str(i+1) + ": " + "Bad magician!\n")
#	print comon
#	print arr1
#	print arr2
#	print i
#	raw_input()
	
	i = i + 1