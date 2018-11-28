
import math
def find_FS(A,B):
	lower=int(math.ceil(math.sqrt(A)))
	upper=int(math.sqrt(B))

	#print lower,upper
	return find_S(lower,upper)

def find_S(A,B):
	count=0
	for i in range(A,B+1):
		s=str(int(i))
		if s==s[::-1]:
			s2=str(i**2)
			if s2==s2[::-1]:
				count=count+1
	return count







f=open("./small.txt")
#t number of games
t=int(f.readline()[:-1])
with open('./out.txt','w') as fout:
	for i in range(1,t+1):
		if i==t:
			line=f.readline().split(" ")
		else:
			line=f.readline()[:-1].split(" ")
		A=int(line[0])
		B=int(line[1])
		s='Case #%i: %s\n' %(i,find_FS(A,B))
		fout.write(s)
