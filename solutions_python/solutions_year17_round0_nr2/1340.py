import fileinput
counter = 0
for line in fileinput.input():
	if not fileinput.isfirstline():
		sol = [i for i in line.strip()]

		while (sorted(sol) != sol):
			#print(sol)
			for i in range(len(sol)-1):
				if sol[i] > sol[i+1]:
					break;
			sol[i] = str(int(sol[i]) - 1)
			for j in range(i+1, len(sol)):
				sol[j] = '9'

		counter += 1
		print("Case #%d: %d" % (counter, int(''.join(sol))))
