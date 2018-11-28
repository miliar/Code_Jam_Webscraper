import fileinput

case = 0
for line in fileinput.input():
	if case == 0:
		case = 1
		continue
	A,B,K = line.split()

	result = [1 for i in range(int(A)) for j in range(int(B)) if i&j in range(int(K))]
	print "Case #"+str(case)+": "+str(len(result))
	case+=1