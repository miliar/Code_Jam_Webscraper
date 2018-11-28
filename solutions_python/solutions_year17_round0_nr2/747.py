import sys, string

if len(sys.argv) == 2:
	try:
		f = open(sys.argv[1], 'r')
	except IOError:
		print("usage python [curr_testing_file] [input_file_name]")
		sys.exit(1)
	
	c = int(f.readline())
	outputs = []

	for i in range(0, c):
		test = f.readline()

		while test == '\n':
			test = f.readline()

		number = list(test)
		number[len(number) - 1] = ''
		last = len(number) - 2
		done = 0
		prev = -1

		if len(number) == 2:
			print("Case #" + str(i + 1) + ": " + "".join(str(x) for x in number))
			#print("Case #" + str(i) + ": " + test)
		else:
			while not done:
				for n in xrange(last, -1, -1):
					if prev == -1:
						prev = int(number[n])
					else:
						if int(number[n]) > prev:
							number[n] = str(int(number[n]) - 1)
							
							for x in xrange(last, n, -1):
								number[x] = '9'
							
							last = n
							prev = -1
							break
						else:
							prev = int(number[n])
				
				if prev != -1:
					done = 1
					
					if number[0] == '0':
						number[0] = ''
					print("Case #" + str(i + 1) + ": " + "".join(str(x) for x in number))
