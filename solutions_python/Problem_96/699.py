n = input()

for i in range(n):
	line = raw_input().split()
	T = int(line[0])
	S = int(line[1])
	p = int(line[2])

	acum = 0
	for j in range(T):
		n = int(line[j+3])

		if p > 0:
			if n / p >= 3:
				acum += 1
			elif n / p == 2:
				if p - (n % p) <= 2:
					acum += 1
				elif p - (n % p) <= 4:
					if S > 0:
						S -= 1
						acum += 1
			elif n/p == 1:
				if (n % p) >= 2*(p-1):
					acum += 1
				elif (n % p) >= 2*(p-2):
					if S > 0:
						S -= 1
						acum += 1


		else:
			acum+=1
		
	print "Case #" + str(i+1) + ": " + str(acum)

