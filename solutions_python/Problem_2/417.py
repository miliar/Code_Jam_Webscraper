#.........calculate ().................
def calcTrains(AA,AD,BA,BD,NA,NB):

	Na = 0
	Nb = 0
        AA.sort()
        AD.sort()
        BA.sort()
        BD.sort()
        AD.reverse()
        BD.reverse()
        for i in range(0,NA):
            if BD != [] and AA[i] >= BD[-1]:
                BD.pop()
            else:
                Na += 1
        for i in range(0,NB):
            if AD != [] and BA[i] >= AD[-1]:
                AD.pop()
            else:
                Nb += 1               
        return Na,Nb

#................................. __main()__ ...............
Input = open("B-small-attempt1.in")
Output = open ("B-Small.out","w")

NoOfCases = int(Input.readline()[:-1])

for i in range(0,NoOfCases):
	TurnArroundTime = float(Input.readline()[:-1])/60		#convert to hrs
	NA,NB = Input.readline()[:-1].split(" ")
	NA = int(NA)
	NB = int(NB)
	ListAA = []
	ListAD = []
	for j in range(0,NA):
		L = Input.readline()[:-1].split(" ")
		ListAA.append(float(L[0].split(":")[0]) + float(L[0].split(":")[1])/60)
		ListAD.append(float(L[1].split(":")[0]) + float(L[1].split(":")[1])/60 +TurnArroundTime)
	
	ListBA = []
	ListBD = []
	for j in range(0,NB):
		L = Input.readline()[:-1].split(" ")
		ListBA.append(float(L[0].split(":")[0]) + float(L[0].split(":")[1])/60)
		ListBD.append(float(L[1].split(":")[0]) + float(L[1].split(":")[1])/60 +TurnArroundTime)
	
	Na,Nb = calcTrains(ListAA,ListAD,ListBA,ListBD,NA,NB)
	Write = "Case #"+ str(i+1) + ": " + str(Na) + " " + str(Nb) + "\n"
	Output.writelines(Write)
	print Na,Nb
	
Input.close()
Output.close()
