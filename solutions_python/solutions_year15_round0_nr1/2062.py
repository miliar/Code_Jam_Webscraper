infile = open("input.txt",'r').read().split('\n')
count = int (infile[0])
for i in range(1, count+1):		
		line = infile[i].split()
		no_of_shy = line [0]
		shy_arr = []
		for a in line [1]:
			shy_arr.append (a)
		count = 0
		no_of_friends = 0
		for shy_iter in range (0, len (shy_arr)):
			if int(shy_arr[shy_iter]) != 0:
				count = count+int(shy_arr[shy_iter])
			if count <= shy_iter:
				no_of_friends = no_of_friends + 1
				count = count + 1

		print "Case #" + str(i) + ": " + str (no_of_friends)


