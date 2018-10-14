import math
def palindrome(pali):
	for i in range(0,len(pali)/2):
		if pali[i]!=pali[-1*(i+1)]:
			return False
	return  True
	
def check(input):
	for i in range(0,len(input)+1):
		if (input[i]==" "):
			output=[0,0]
			output[0]=input[:i]
			output[1]=input[i+1:]
			return output

T=int(raw_input())

answers=[]

for i in range(0,T):
	answers.append(0)
	enter=raw_input()
	enters=check(enter)
	
	a=int(enters[0])
	b=int(enters[1])
	for j in range(a,b+1):
		if int(math.sqrt(j))**2==j:
			if palindrome(str(j))==True:
				if palindrome(str(int(math.sqrt(j))))==True:
					answers[i]+=1
	
for i in range(0,T):
	print "Case #%s: %s" % (i+1,answers[i])
	
	