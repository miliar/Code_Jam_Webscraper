f = open("input")

T = int(f.readline())

for tc in range(0, T):

	line = f.readline()
	tab  = line.split()

	N  =  int(tab[0])
	S  =  int(tab[1])
	P  =  int(tab[2])

	Res = 0

	for n in range(0, N):
		
		Total = int(tab[n + 3])
		Reste = Total % 3
		Min   = Total / 3
		Max   = Min

		if Reste == 0:		
			if Max >= P:
				Res = Res + 1
			elif Max + 1 >= P and S > 0 and Total <> 0:
				Res = Res + 1
				S   = S   - 1

		elif Reste == 1:
			Max = Max + 1
			if Max >= P:
				Res = Res + 1

		elif Reste == 2:
			Max = Max + 1
			if Max >= P:
				Res = Res + 1
			elif Max + 1 >= P and S > 0:
				Res = Res + 1
				S   = S   - 1
		
		#print ("Total = %d, Min = %d, Reste = %d, Max = %d, P = %d, S = %d, Res = %d" % (Total, Min, Reste, Max, P , S, Res))


	print ("Case #%d: %d" % (tc + 1, Res))
		
			
			
			
			 
