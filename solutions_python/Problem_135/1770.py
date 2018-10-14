from sys import stdin,stdout

for t in range(int(stdin.readline())):
	arrangement_1=[]
	arrangement_2=[]
	volunteer_choice = int(stdin.readline())

	for i in range(4):
		arrangement_1.append(list(map(int,stdin.readline().split())))
	volunteer_choice_2 = int(stdin.readline())
	
	for i in range(4):
		arrangement_2.append(list(map(int,stdin.readline().split())))

	count = 0
	common=0

	for x in arrangement_1[volunteer_choice -1]:
		if x in arrangement_2[volunteer_choice_2 -1]:
			common = x
			count += 1
	#print (count,common)
	if count==1:
		print('Case #'+str(t+1)+': '+str(common))
	elif count == 0:
		print('Case #'+str(t+1)+': Volunteer cheated!')
	else:
		print('Case #'+str(t+1)+': Bad magician!')


