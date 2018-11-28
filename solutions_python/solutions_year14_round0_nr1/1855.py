case=int(input())
z=1
while case>=z:
	grid1=[]
	grid2=[]
	choice1=int(input())
	for i in range(0,4):
		s=input()
		grid1.append(s.split(' '))
	choice2=int(input())
	for i in range(0,4):
		s=input()
		grid2.append(s.split(' '))
	final=set(grid1[choice1-1]).intersection(set(grid2[choice2-1]))
	if len(final)==1:
		x=list(final)		
		print("Case #"+str(z)+": "+str(x[0]))
	elif len(final)>1:
		print("Case #"+str(z)+": Bad magician!")
	else:
		print("Case #"+str(z)+": Volunteer cheated!")
	z+=1
