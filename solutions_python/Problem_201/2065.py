import copy
import numpy
import sys
sys.setrecursionlimit(1500)
        
class HeapMAX:
    
    global beEl
    
    def __init__(self):
        self.array=[]
        self.brEl=0
        
    def Swap(self,x,y):
        pom=copy.deepcopy(self.array[x])
        self.array[x]=copy.deepcopy(self.array[y])
        self.array[y]=copy.deepcopy(pom)
        
    def BubbleUp(self,n):
        if n==0:
            return
    
        if (n%2):
            donji=int(numpy.floor(n/2))
            if self.array[donji][0]<self.array[n][0]:
                self.Swap(donji,n)
                self.BubbleUp(donji)
        else:
            donji=n//2-1
            if self.array[donji][0]<self.array[n][0]:
                self.Swap(donji,n)
                self.BubbleUp(donji)
    
    def BubbleDown(self,n):
        
        if len(self.array)<=1:
            return
        
        if len(self.array)==2:
            if self.array[1][0]>self.array[0][0]:
                self.Swap(0,1)
            return
        
        if (2*n+1>len(self.array)-1):
            return
            
        if (2*n+2>len(self.array)-1):
            if self.array[2*n+1][0]>self.array[n][0]:
                self.Swap(2*n+1,n)
                self.BubbleDown(2*n+1)
            return
        
        if ((self.array[(n+1)*2][0]>=self.array[2*n+1][0]) and (self.array[(n+1)*2][0]>self.array[n][0])):
            self.Swap((n+1)*2,n)
            self.BubbleDown((n+1)*2)
            return
            
        if ((self.array[(n+1)*2][0]<self.array[2*n+1][0]) and (self.array[n*2+1][0]>self.array[n][0])):
            self.Swap(2*n+1,n)
            self.BubbleDown(2*n+1)
            return
            
    def HEAPIFY(self,A):
        self.brEl+=len(A)
        self.array=copy.deepcopy(A)
        for i in range(int(numpy.floor(len(A)/2))+1):
            n=int(numpy.floor(len(A)/2))-i
            self.BubbleDown(n)
        
    def INSERT(self,a):
        self.array.append(a)
        self.brEl+=1
        self.BubbleUp(len(self.array)-1)
        
    def EXTMAX(self):
        pom=copy.deepcopy(self.array[0])
        self.brEl-=1
        if len(self.array)!=1:
            self.array[0]=self.array.pop()
        else:
            self.array=[]
        self.BubbleDown(0)
        return pom
        
    def PEAK(self):
        return self.array[0]
        
    def DELETE(self,a):
        if a not in self.array:
            return
        self.brEl-=1
        if len(self.array)==1:
            self.array=[]
            return
        n=self.array.index(a)
        self.array[n]=self.array.pop()
        self.BubbleDown(n)

def FinishedFunction(NN,KK):

	global stalls
	global idx
	global pairs
	global N

	N = NN
	K = KK

	import sys
	sys.setrecursionlimit(1500)

	stalls = [0]*N
	pairs = HeapMAX()
	idx = 0

	def AssignStalls(l,r, K):
	
		global stalls
		global idx
		global pairs
		global N
	
		stalls[(r+l)//2]=1
		if K<=1:
			idx = (r+l)//2
			return
	
		if (l<=(r+l)//2 and l>=0):
			if ((stalls[(r+l)//2-1])==0 and stalls[l]==0):
				p1 = [(l-((r+l)//2-1))**2,l,(r+l)//2-1]
				pairs.INSERT(p1)
	
		if (r<N and r>=(r+l)//2 and (r+l)//2+1<N):
			if (stalls[(r+l)//2+1])==0:
				p2 = [((r+l)//2+1 - r)**2,(r+l)//2+1,r]
				pairs.INSERT(p2)
	
		target = pairs.EXTMAX()
		AssignStalls(target[1],target[2],K-1)
	

	AssignStalls(0,N-1,K)
	lidx = idx - 1
	ridx = idx + 1
	Ls = 0
	if lidx>=0:
		while (stalls[lidx]==0):
			Ls+=1
			lidx-=1
			if lidx==-1:
				break
	Rs = 0
	if ridx<N:
		while (stalls[ridx]==0):
			Rs+=1
			ridx+=1
			if (ridx==N):
				break
	del pairs
	return (max(Ls,Rs),min(Ls,Rs))

		


with open('/Users/gorankovacevic/Desktop/D&A of Algos/Google/Code Jam Practice/stalls/C-small-1-attempt0.txt') as f:
	a = []
	for line in f:
		line = line.split()
		a.append(line)
		
fout = open('/Users/gorankovacevic/Desktop/D&A of Algos/Google/Code Jam Practice/stalls/C-small-1-attempt0Out.txt', 'w')
		
NNN = int(a[0][0])
case = 1

A = []
for i in range(1,len(a)):
	curr = []
	for j in range(len(a[i])):
		curr.append(int(a[i][j]))
	A.append(curr)

for i in range(len(A)):
	
	NN = A[i][0]
	KK = A[i][1]
	F, S = FinishedFunction(NN,KK)

	out1 = str(F)
	out2 = str(S)
	out2+='\n'
	fout.write("Case #" + str(case) + ": " + out1 + " " + out2)
	case += 1
