#number of testcases
numCases = int(input())

for case in range( 1,numCases + 1 ) :
	test_data = input()
	data = test_data.split()

	#R is the number of rides in a day
	R = int(data[0])
	#K is the capacity of the roller coaster
	K = int(data[1])
	#N is the number of groups of person willing to ride
	N = int(data[2])

	g = input()
	group = g.split() #group is the list of proper ordering of groups in queue

	#change into an integer list
	for i in range(len(group)) :
		group[i] = int(group[i])
				
	earning = 0
	#toapp = [] #here the elements will be popped

	for trip in range(1,R+1) : #for each trip
		toapp = [] #again initialize toapp
		sum = group[0]  # sum is the earning in each trip
		toapp.append(group.pop(0)) #pop and append it to app
	
		spaceLeft = True
		while spaceLeft == True and len(group) != 0 :
			if (sum + group[0]) <= K :
				sum = sum + group[0]
				toapp.append(group.pop(0)) #pop and append
		
			else :
				spaceLeft = False

		earning = earning + sum
		#again append the toapp to group
		group.extend(toapp)
	print('Case #'+str(case)+':'+' ' +str(earning))
