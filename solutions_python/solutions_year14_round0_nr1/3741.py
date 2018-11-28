cases= int(raw_input())
i=''
printList=[]
cur=0
while (cur<cases):
	guess1=int(raw_input())
	i=0
	while(i<4):
		
		if(i+1==guess1):
			listOfWords1=raw_input().rsplit(' ')
		else:
			raw_input()

		i+=1

	guess2=int(raw_input())
	i=0
	while(i<4):
		
		if(i+1==guess2):
			listOfWords2=raw_input().rsplit(' ')
		else:
			raw_input()

		i+=1
	finalList=list(set(listOfWords1) & set(listOfWords2))
	if(len(finalList))==1:
		print("Case #"+ str(cur+1)+ ": " + finalList[0])

	elif(len(finalList)>1):
		print("Case #"+ str(cur+1)+ ": " + "Bad magician!")

	else:
		print("Case #"+ str(cur+1)+ ": " + "Volunteer cheated!")

		
	cur+=1

	