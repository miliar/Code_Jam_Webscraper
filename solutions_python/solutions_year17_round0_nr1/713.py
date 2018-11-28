import sys, string

if len(sys.argv) == 2:
	try:
		f = open(sys.argv[1], 'r')
	except IOError:
		print("usage: python pancake.py [input_file_name]")
		sys.exit(1)
	
	c = int(f.readline())
	outputs = []

	for i in range(0, c):
		test = f.readline()

		while test == '\n':
			test = f.readline()

		s = list(test.split(' ')[0])
		k = int(test.split(' ')[1])
		count = 0
		imp = 0

		for n in range(0, len(s)):
			if s[n] == '-':
				if n + k > len(s):
					print("Case #" + str(i + 1) +": IMPOSSIBLE")
					imp = 1
					break
				else:
					for x in range(n, n + k):
						if s[x] == '+':
							s[x] = '-'
						else:
							s[x] = '+'
					count += 1

		if imp != 1:
			for v in range(0, len(s)):
				if s[v] == '-':
					print("Case #" + str(i + 1) +": IMPOSSIBLE")
					imp = 1
					break

			if imp != 1:
				print("Case #" + str(i + 1) +": " + str(count))
