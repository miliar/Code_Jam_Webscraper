import copy


f = open('input.txt', 'r')
amount = f.readline()
amount = int(amount)
qw = 0
stringAll = ''
money =0
for qw in range(amount):
	
	temp1 = f.readline().split(' ')
	N = int(temp1[0]) #total chickens
	K = int(temp1[1]) #chickens that have to arrive
	B = int(temp1[2]) #distance to barn
	T = int(temp1[3]) #no later than this time
	temp1 = f.readline().split(' ')
	pos = temp1

	temp1 = f.readline().split(' ')
	speed = temp1
	speedBack = [[]]*N
	posBack = [[]]*N
	for i in range(N):
		amount = 0
		swapCount = 0
		speed[i] = int(speed[i])
		speedBack[i] = int(speed[i])
		pos[i] = int(pos[i])
		posBack[i] = int(pos[i])
		#http://stackoverflow.com/questions/2541865/copying-2d-lists-in-python
	for i in range(N):
		#print pos[N-i-1]+speed[N-i-1]*(T)
		
		if(amount != K and pos[N-i-1]+speed[N-i-1]*(T) >= B):
			swapCount = swapCount + i-amount
			
			amount = amount+1
			#print 'can make it anout'+str(amount)
	
	swapsNeeded = swapCount
	if (amount != K):
		swapsNeeded="IMPOSSIBLE"
	
	stringAll+="Case #" + str(qw+1) + ": "+str(swapsNeeded) +"\n"
	print "Case #" + str(qw+1) + ": "+str(swapsNeeded)


f = open('out.txt', 'w')
f.write(stringAll)
