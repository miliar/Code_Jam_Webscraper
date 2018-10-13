output=list()
def Prob1():
	f=open('input1Small.txt','r')
	t=int(f.readline())
	for i in range(t):
		D,N=map(int,f.readline().strip().split())
		m=0
		for j in range(N):
			R,S=map(int,f.readline().strip().split())
			x=float((D-R)/S)
			if x>m:
				m=x
		output.append(round(D/m,6))
	f.close()
	writeOutput()

def writeOutput():
	f=open('output1Small.txt','w')
	for i in range(len(output)):
		print("Case #"+str(i+1)+": "+str(output[i]))
		f.write("Case #"+str(i+1)+": "+str(output[i])+'\n')
	f.close()
Prob1()
