input = file('C-small-attempt0.in')
output = file('out','w')
numberOfCase = int(input.readline())
for i in range(1, numberOfCase+1):
	money = 0
	(r, k, n) = [int(x) for x in input.readline().split()]
	q = [int(x) for x in input.readline().split()]
	for j in range(r): #run
		passenger = []
		numofpassenger = 0
		for l in range(len(q)): #adding passenger
			if(numofpassenger+q[0] > k or len(q)==0):
				break
			numofpassenger += q[0]
			passenger.append(q[0])
			q = q[1:]
		money += numofpassenger
		q.extend(passenger)
	output.write("Case #"+str(i)+": "+ str(money))
	output.write("\n")
