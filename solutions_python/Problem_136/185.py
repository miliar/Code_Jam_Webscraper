file = open('input', 'r')

problems = int(file.readline())

for i in range(1, problems+1):
	values = file.readline().split()
	C = float(values[0])
	F = float(values[1])
	X = float(values[2])
	F_t = 2 # total cookie production
	T_t = 0.0 # total Time
	while True:
		if (X-C) / F_t < X / (F_t + F):
			T_t = T_t + X / F_t
			print 'Case #' + str(i) + ': ' + str(T_t)
			break # exit loop
		else:
			T_t = T_t + C / F_t
			F_t = F_t + F
