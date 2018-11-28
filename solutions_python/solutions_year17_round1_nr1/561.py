from collections import Counter
output=list()
def Prob1():
	f=open('input1Large.txt','r')
	t=int(f.readline())
	for i in range(t):
		[R,C] =list(map(int,f.readline().split()))
		#print(R,C)
		lst=list()
		first=''
		for j in range(R):
			line=f.readline().rstrip()
			lst.append(list(line))
		calcHorizontal(lst,R,C)
		calcVertical(lst,R,C)
		calcHorizontal(lst,R,C)
		calcVertical(lst,R,C)
		#print(lst)
		output.append(lst)
	f.close()
	writeOutput()

def calcHorizontal(l,R,C):
	for i in range(R):
		for j in range(C):
			if l[i][j]!='?':
				for k in range(j-1,-1,-1):
					if l[i][k]=='?':
						l[i][k]=l[i][j]
		for j in range(C-1,-1,-1):
			if l[i][j]!='?':
				for k in range(j+1,C):
					if l[i][k]=='?':
						l[i][k]=l[i][j]

def calcVertical(l,R,C):
	for i in range(C):
		for j in range(R):
			if l[j][i]!='?':
				for k in range(j-1,-1,-1):
					if l[k][i]=='?':
						l[k][i]=l[j][i]
		for j in range(R-1,-1,-1):
			if l[j][i]!='?':
				for k in range(j+1,R):
					if l[k][i]=='?':
						l[k][i]=l[j][i]

def writeOutput():
	f=open('output1Large.txt','w')
	for i in range(len(output)):
		print("Case #"+str(i+1)+":")
		f.write("Case #"+str(i+1)+":\n")
		for j in range(len(output[i])):
			print(''.join(output[i][j]))
			f.write(''.join(output[i][j])+'\n')

Prob1()
