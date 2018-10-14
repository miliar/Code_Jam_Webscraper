f=open("input.txt","r")
T=int(f.readline())
cases=f.readlines()
f.close()
open("ans.txt","w").close()

numcase=0

for case in cases:

	numcase=numcase+1

	case=case[0:len(case)-1]
	maxShyLevel=int(case[0])
	shyString=case[2:len(case)]

	maxProblem=0
	flag=True

	while(flag):

		numPeople=maxProblem

		for shyLevel in range(maxShyLevel+1):

			if numPeople >= shyLevel :
				numPeople = numPeople + int (shyString[shyLevel])
				flag=False

			else :
				maxProblem=maxProblem+1
				flag=True
				break

	f=open("ans.txt","a")
	f.write("Case #"+str(numcase)+": "+str(maxProblem)+"\n")
	f.close()


