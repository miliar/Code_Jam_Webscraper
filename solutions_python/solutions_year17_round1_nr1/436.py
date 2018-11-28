import time

t0 = time.time()


with open("/Users/andrewKyres/Downloads/A-large (1).in") as f:
	with open("/Users/andrewKyres/Downloads/google.out", "w+") as out:
		T = int(f.readline())
		for t in xrange(1, T+1):
			line = f.readline()
			splitter = line.split(' ')
			R = int(splitter[0])
			C = int(splitter[1])

			cake = [[0 for x in range(R)] for y in range(C)] 
			for j in xrange(0, R):
				line = f.readline()
				splitter = list(line)
				for k in xrange(0, C):
					cake[k][j] = splitter[k]

			blanks = set()
			for i in xrange(0,R):
				initial = '?'
				for j in xrange(0,C):
					if cake[j][i] != '?':
						initial = cake[j][i]
					if cake[j][i] == '?' and initial != '?':
						cake[j][i] = initial

				# collect blank rows
				if initial == '?':
					blanks.add(i)
					continue

				# go backwards now to make sure none have been missed
				initial = '?'
				for j in xrange(C-1,-1, -1):
					if cake[j][i] != '?':
						initial = cake[j][i]
					if cake[j][i] == '?' and initial != '?':
						cake[j][i] = initial

			# handle blank rows
			initial = []
			for i in xrange(0,R):
				if i not in blanks:
					initial = []
					for j in xrange(0,C):
						initial.append(cake[j][i])

				if i in blanks and initial:
					for j in xrange(0,C):
						cake[j][i] = initial[j]
					blanks.remove(i)

			# repeat backwards
			initial = []
			for i in xrange(R-1,-1,-1):
				if i not in blanks:
					initial = []
					for j in xrange(0,C):
						initial.append(cake[j][i])

				if i in blanks and initial:
					for j in xrange(0,C):
						cake[j][i] = initial[j]

			# output = calc(x,y)
			out.write("case #%s:\n" % (t))
			for i in xrange(0,R):
				for j in xrange(0,C):
					out.write(cake[j][i])
				out.write("\n")

t1 = time.time()
print t1-t0

