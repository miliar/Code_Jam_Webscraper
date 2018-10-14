import sys
sys.stdin = open('A-large.in','r')
sys.stdout = open('output.txt','w')

def swap(start,string,panSize):
	
	for i in range(panSize):
	
		if(string[start+i] == "+"):
			string[start+i] = "-"
		else:
			string[start+i]="+"
	
	return string

def check(string,panSize):
	counter=0
	
	for i in range(len(string)):
		if(string[i]=="-"):
			if(len(string)-i>=panSize):
				string=swap(i,string, panSize)
				counter+=1
	return[counter,string]


for i in range(int(input())):
	string2,panSize=input().split(" ")
	panSize=int(panSize)
	string=[k for k in string2]

	lis=check(string,panSize)
	
	flag=False
	for j in (lis[1]):
		if(j=="-"):
			flag=True

	
	if(flag==False):
		print("Case #"+str(i+1)+": "+str(lis[0]))
	else:
		print("Case #"+str(i+1)+": IMPOSSIBLE")
