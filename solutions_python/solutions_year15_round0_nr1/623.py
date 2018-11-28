def displayArray(my_array):
	for i in range(len(my_array)):
		print i

for tc in range(1, int(raw_input())+1):
	#print 
	y = ''


	#Everyone in the audience has a shyness level. 
	#An audience member with shyness level Si will wait until at least S other audience members have already stood up to clap,
	# and if so, she will immediately stand up and clap


	Smax, S = raw_input().split()

	countNbPersonInTheAudience = 0

	shyness =[]
	peopleAlreadyStandUp = 0
	for i in str(S):
		countNbPersonInTheAudience += int(i)
		shyness.append(i)
	#print 'countNbPersonInTheAudience', countNbPersonInTheAudience

	#print 'shyness', shyness

	peopleAlreadyStandUp = int(shyness[0])
	#print 'peopleAlreadyStandUp', peopleAlreadyStandUp
	
	NumberOfPersonAdded = 0
	for posLevel in range(1,len(shyness)):
		#print 'posLevel', posLevel
		if peopleAlreadyStandUp >= posLevel:
			#print 'IF peopleAlreadyStandUp, posLevel', peopleAlreadyStandUp, posLevel
			peopleAlreadyStandUp += int(shyness[posLevel])
		else:
			#print 'ELSE peopleAlreadyStandUp, posLevel', peopleAlreadyStandUp, posLevel
			personsNeeded = posLevel - peopleAlreadyStandUp #- shyness[posLevel]
			peopleAlreadyStandUp += personsNeeded + int(shyness[posLevel])   ###NOW YOU CAN ADD OTHERS
			NumberOfPersonAdded += personsNeeded



	#print 'NumberOfPersonAdded', NumberOfPersonAdded

	#print S
	#print S.split("")

	#count = sum(map(int,S.split()))

	#print count

	#Smax the maximum shyness level of the shyest person in the audience

	# For example, the string "409" would mean that there were four audience members with Si = 0 
	#and nine audience members with Si = 2
	#and none with Si = 1 or any other value).
	# Note that there will initially always be between 0 and 9 people with each shyness level.


	#N, P = map(int, raw_input().split())



	#y is the minimum number of friends you must invite.
	#if y != ''
	print "Case #{}: ".format(tc) + str(NumberOfPersonAdded)
	#else:
	#print "Case #{}".format(tc) + stry(y)
		
	
