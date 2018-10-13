input = open('input.txt', 'r')
outputf = open('output.txt', 'w')

T = int(input.readline())

for tc in range(1, T+1):
	row = input.readline().rstrip().split(" ")
	C = float(row[0])
	F = float(row[1])
	X = float(row[2])
	
	Ta = X / 2.0
	
	Tfarms = C / 2.0
	n = 1

	Tb = Tfarms + X / ( 2.0 + F )
	
	while Tb < Ta:
		Ta = Tb
		n+=1
		Tfarms += C / ( 2 + (n -1) * F)
		Tb = Tfarms + X / (2 + n * F)
	
	outputf.write("Case #" + str(tc) + ": " + str(Ta) + "\n")