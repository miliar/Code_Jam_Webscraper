T = int(raw_input())
def solve(N,S,p,score):
	count = 0
	score2=list(score)
	to_remove = []
	for i in range(N):
		if(score[i]/3>=p):
			count+=1
			#to_remove.append(i)
		elif(score[i]/3 == p-1 and score[i]%3>0):
			count+=1
			#print "hi2",score[i]
			#to_remove.append(i)
		elif(S>0):
			if(score[i]/3 == p-2 and score[i]%3==2):
				S-=1;
				count+=1;
			elif(score[i]/3==p-1 and p-1>0):#and score2[i]%3==0):
				count+=1;
				S-=1;
	#for i in range(N):
	#	if(not i in to_remove):
	#		score2.append(score[i])
	#for i in range(len(score2)):
	#	if(S==0):
	#		break;
	#	if(score2[i]/3 == p-2 and score2[i]%3==2):
	#		S-=1;
	#		count+=1;
	#	elif(score2[i]/3==p-1 and p-1>0):#and score2[i]%3==0):
	#		print "hi2",score2[i]
	#		count+=1;
	#		S-=1;
	return count;
	
for Ti in range(T):
	score = [int(x) for x in raw_input().split(' ')]
	N,S,p = score[:3]
	score = score[3:]
	print "Case #%d: %d"%(Ti+1,solve(N,S,p,score))
	
