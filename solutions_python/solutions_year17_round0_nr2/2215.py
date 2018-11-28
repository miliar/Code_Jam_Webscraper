from collections import Counter
output=list()
#lst=list()
def Problem2():
	f=open('input2.txt','r')
	n=int(f.readline())
	for i in range(n):
		inp=int(f.readline())
		tmp=calc(list(map(int,str(inp))))
		#print(tmp)
		while(tmp[0]=='True'):
			#print(tmp[0],tmp[1])
			tmp=calc(tmp[1])
	writeOutput()

def calc(l):
	#print(l)
	if len(l)==1:
		output.append(l[0])
		return str(False)
	for i in range(1,len(l)):
		if l[i-1]>l[i]:
			s=list()
			if l[i]!=0:
				s.extend(l[:i-1])
				s.append(l[i-1]-1)
				s.extend([9]*(len(l)-i))
			else:
				s.extend(l[:i-1])
				s.append(l[i-1]-1)
				s.extend([9]*(len(l)-i))
			#input(s)
			return (str(True),s)
	output.append(int(''.join(map(str,l))))
	return str(False)

#def calc2(n):


def writeOutput():
	f=open('output2.txt','w')
	for i in range(len(output)):
		f.write("Case #"+str(i+1)+": "+str(output[i])+'\n')
	f.close()

Problem2()