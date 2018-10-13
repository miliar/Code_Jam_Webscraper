finput = open("inputc.txt", "r")
foutput = open("outputc.txt", "w")

def check_shit(a, b):

	result=0

	for i in range(a,b):
		
		number = str(i)
		pairs = set([])

		for j in range(len(number)):
			number=number[1:]+number[0]
			m=int(number)
			if m>i and m<=b:
				pairs.add(m)

		result += len(pairs)

	return result

t=int(finput.readline())

for i in range(t):
	ints = finput.readline().split()
	a, b = int(ints[0]), int(ints[1])
	result = check_shit(a,b)

	foutput.write("Case #" + str(i+1) + ": " + str(result) + "\n")


finput.close()
foutput.close()