

Matrix = [["" for y in xrange(4)] for x in xrange(4)]
MatrixResult1=["" for x in xrange(4)]
MatrixResult2=["" for x in xrange(4)]
MatrixFinal=["" for x in xrange(4)]
T=0
TT=0
TTT=0
LINE=0

def ReadInput():
	f = open("A-small-attempt1.in","r")
	ListOfLetters = f.readlines()
	i=1
	w=0
	counter=1
	global T , TT , TTT
	f.close()
	f = open("Result.txt","w")
	f.close
	for text in ListOfLetters:
		if(len(text)<=4 and i==1):
			T=int(text)
		if(len(text)<=2 and i==2):
			TT=int(text)
		if(len(text)<=2 and i==3):
			TTT=int(text)
			i=1
		if(len(text)>5):
			Matriz=text.split()
			FillMatrix(Matriz)
			w=w+1
			if w==4:

				if i==3:
					FillRowResult(TT,1)
				if i==2:
					FillRowResult(TTT,2)
					f = open("Result.txt","a")
					f.write("Case #"+str(counter)+": "+Logic()+"\n")
					counter=counter+1
					f.close
				w=0
		if (i<3 and len(text)<=4):			
			i=i+1					
			



def FillMatrix(Matriz):
	global LINE
	for i in range(4):
		Matrix[i][LINE]=Matriz[i]
	LINE=LINE+1
	if LINE>=4:
		LINE=0


def FillRowResult(TT , MatType):
	if MatType==1:
		for i in range(4):
			MatrixResult1[i]=Matrix[i][TT-1]
	else:
		for i in range(4):
			MatrixResult2[i]=Matrix[i][TT-1]		

def Logic():
	Result=""
	g=0
	for x in range(4):
		MatrixFinal[x]=""	
	for i in range(4):
		for w in range(4):
			if(MatrixResult1[i]==MatrixResult2[w]):
				MatrixFinal[g]=MatrixResult1[i]
				if (MatrixFinal[g]!=""):
					g=g+1
	if (MatrixFinal[0]==""):
		Result="Volunteer cheated!"	
		return Result
	if (MatrixFinal[1]=="") :
		Result=str(MatrixFinal[0])
		return Result
	if (MatrixFinal[1]!=""):
		Result="Bad magician!"
		return Result			
	


def main():
	ReadInput()				


						

			


if __name__=='__main__' :
    main() 			
