import math
n_cases=raw_input()

for t in range(int(n_cases)):
	times=[]
	input_string=raw_input().split()
	ac=int(input_string[0])
	aj=int(input_string[1])

	for line in range(ac):
		s=raw_input().split()
		times+=[ (int(s[0]),int(s[1]),0) ]

	for line in range(aj):
		s=raw_input().split()
		times+=[ (int(s[0]),int(s[1]),1) ]

	times.sort(key=lambda x: x[0])
	
	adjustable=[0,0]
	paid_adjustable=[[],[]]
	time_act=[0,0]
	
	changes=0
	cur=times[0][2]
	time_act[cur]=times[0][0] #add time from 0 to start of first activity

	for i in range(1,len(times)):
		if times[i][2]!=cur: #change
			time_act[cur]+=(times[i][0]-times[i-1][0])
			changes+=1
			if cur==0:
				adjustable[0]+=(times[i][0]-times[i-1][1])
			else:
				adjustable[1]+=(times[i][0]-times[i-1][1])
			cur=times[i][2]
		else: #keep
			time_act[cur]+=(times[i][0]-times[i-1][0])
			paid_adjustable[cur]+=[times[i][0]-times[i-1][1]]

	time_act[cur]+=(1440-times[len(times)-1][0])
	
	if cur!=times[0][2]:
		changes+=1
		time_act[cur]+=times[0][0]
		time_act[1-cur]-=times[0][0]
		adjustable[cur]+=(1440-times[len(times)-1][1])
		adjustable[cur]+=times[0][0]
	else:
		paid_adjustable[cur]+=[ (1440-times[len(times)-1][1]) + times[0][0] ]

	#print(adjustable)
	#print(time_act)
	#print(paid_adjustable)

	paid_adjustable[0].sort(key=lambda x: -x)
	paid_adjustable[1].sort(key=lambda x: -x)
	
	if time_act[0]==720 or (time_act[0]<720 and adjustable[1]>=(720-time_act[0])):
		print('Case #%d: %d' % (t+1,changes))
		continue

	elif time_act[1]==720 or (time_act[1]<720 and adjustable[0]>=(720-time_act[1])):
		print('Case #%d: %d' % (t+1,changes))
		continue

	elif time_act[0]+adjustable[1]<720: #need to transfer activity time to 0
		changes0=changes
		time_0=time_act[0]+adjustable[1]
		i=0
		while time_0<720 and i<len(paid_adjustable[1]):
			time_0+=paid_adjustable[1][i]
			changes0+=2
		if time_0>=720:
			print('Case #%d: %d' % (t+1,changes0))
			continue

	elif time_act[1]+adjustable[0]<720: #need to transfer activity time to 1
		changes1=changes
		time_1=time_act[1]+adjustable[0]
		i=0
		while time_1<720 and i<len(paid_adjustable[0]):
			time_1+=paid_adjustable[0][i]
			changes1+=2
		if time_1>=720:
			print('Case #%d: %d' % (t+1,changes1))
			continue
