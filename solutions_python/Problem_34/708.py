import string, StringIO,re

def challenge1():
	f_small=open('/home/prperold/GoogleCodeJam/Challenge1/Input/in.txt', 'r')
	
	input = f_small.readlines()
	index = 0
	l=""
	d=""
	n=""
	
	while input[0][index].isdigit():
		l+=input[0][index]
		index+=1
	index+=1
	while input[0][index].isdigit():
		d+=input[0][index]
		index+=1
	index+=1
	while input[0][index].isdigit():
		n+=input[0][index]
		index+=1
	
	L = int(l)
	D = int(d)
	N = int(n)
		
	alienwords = ""
	for i in range(0,int(D)):
		temp = ""
		index=0
		while input[i+1][index].isalpha():
			temp+=input[i+1][index]
			index+=1
		alienwords+=temp+" "
	
	testcases=[]	
	for i in range(int(D)+1,(int(D)+int(N))+1):
		temp = ""
		index=0

		while input[i][index].isalpha() or input[i][index]=='(' or input[i][index]==')':
			if input[i][index].isalpha():
				temp+=input[i][index]
			if input[i][index]=='(':
				temp+="["
			if input[i][index]==')':
				temp+="]"
			index+=1
		
		testcases.append(temp)
		
	outputFile(matcher(alienwords,testcases))
	
def matcher(alienwords,testcases):
	out = []
	for i in testcases:
		p = re.compile(i)
		out.append(len(p.findall(alienwords)))
	return out
		
def outputFile(out):
	f_out=open('/home/prperold/GoogleCodeJam/Challenge1/Output/out.txt', 'w')
	for i in range(len(out)):
		f_out.write("Case #"+str(i+1)+": "+str(out[i])+"\n")

if __name__ == "__main__":
    challenge1()
