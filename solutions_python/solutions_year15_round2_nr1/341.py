def read_words(afile):
    words = []
    for line in afile:
            words.append(line.strip())
    return words

filename = open('poop.txt' , 'r')
T = filename.readline() #num test cases
aList = read_words(filename)

for i in range(int(T)):
	N = aList[i]
	count = 0

	while int(N) > 1:
		digits = ((len(N))/2)
		
		if int(N[digits:]) > 1:
			N = str( int(N)-1)
			count += 1
		elif (int(N) > int(N[::-1])) and (int(N[-1]) != 0) :
			N = N[::-1]
			count += 1
		else:
			N = str(int(N)-1)
			count += 1

	print "Case #" + str(i+1) + ": " + str(count+1)
		# if (int(N) > int(N[::-1])) and (int(N[-1]) != 0) :
		# 	# find 1
		# 	derp = len(N)
			
		# 	while (N[derp-1] == "0"):
		# 		derp -= 1
		# 	if (N[derp-1] == "1"):
		# 		N = N[::-1]
		# 		count += 1
		# 	else:
		# 		N = str(int(N)-1)
		# 		count += 1
		# else:
		# 	N = str(int(N)-1)
		# 	count += 1



	