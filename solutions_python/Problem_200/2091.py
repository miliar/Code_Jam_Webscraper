def esTidy(N):
	cad=str(N)
	for i in range(len(cad)):
		if(i>0):
			if(long(cad[i])<long(cad[i-1])):
				return False
	
	return True

def arreglar(N):
	cad=str(N)
	for i in range(len(cad)):
		if(i>0):
			if(long(cad[i])<long(cad[i-1])):
				punto=i
				break
	Z=""
	for i in range(len(cad)):
		if i<=punto:
			Z=Z+str(cad[i])
		else:
			Z=Z+str(0)
	N=long(Z)
	return N
	
def calcular(N):
	#print(N)
	if(esTidy(N)):
		return N

	while (True):		
		#print(N)
		N=arreglar(N)
		if(esTidy(N)):
			return N
		
		if(esTidy(N-1)):
			return N-1
		
		N=N-1

#main
def main():
	R=long(input())
	for A in range(R):
		N=long(input())
		X=calcular(N)
		C=A+1
		print("Case #"+str(C)+": "+str(X))
if __name__ == "__main__":
	# execute only if run as a script
	main()
