rows={}
f = open( "small.in", "r" )
o=open("result.out","w")
testCaseNumber=int(f.readline())

for i in range(testCaseNumber):
	pickedRow1=int(f.readline())
	rows[1]=f.readline().split()
	rows[2]=f.readline().split()
	rows[3]=f.readline().split()
	rows[4]=f.readline().split()
	pickedRow2=int(f.readline())
	rows[5]=f.readline().split()
	rows[6]=f.readline().split()
	rows[7]=f.readline().split()
	rows[8]=f.readline().split()
	
	coincidences=set(rows[pickedRow1]) & set(rows[pickedRow2+4])

	if(len(coincidences)==0):
		print("Volunteer cheated!")
		o.write("Case #"+str(i+1)+": Volunteer cheated!")
	elif(len(coincidences)==1):
		chosenCard=coincidences.pop()
		print(chosenCard)
		o.write("Case #"+str(i+1)+": "+str(chosenCard))
	else:
		print("Bad magician!")
		o.write("Case #"+str(i+1)+": Bad magician!")

	if(i!=testCaseNumber-1):
		o.write("\n")

f.close()

o.close()
