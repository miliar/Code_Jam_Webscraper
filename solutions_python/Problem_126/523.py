#def V(l):
#	if l=="a" or l=="e" or l=="i" or l=="o" or l=="u":return 1
#	return 0 

def C(l):
	if l=="a" or l=="e" or l=="i" or l=="o" or l=="u":return 0

	return 1

def count(a,b):#Find if string a has b consecutive consonants
	if b==0:return 1
	if len(a)==0:return 0
	if len(a)<b:return 0
	for k in range(0,len(a)-b+1):

		if min(map(lambda x:C(a[k+x]),range(0,b)))==1:return 1

	return 0

def calculate(a,b):#Calculate b-value of string a, process all substrings
	m=0
	for i in range(0,len(a)):
		if i!=len(a): m+=sum(map(lambda x:count(a[i:x+1],b),range(i,len(a))))
		#for j in range(i,len(a)):
		#	m+=count(a[i:j],b)
		if i==len(a):m+=count(a[i],b)
		
	return m

def main():
	NTC=int(raw_input())
	for TCN in range(1,NTC+1):
		[A,B]=raw_input().split()
		B=int(B)	
		output=calculate(A,B)
		print "Case #"+str(TCN)+": "+str(output)
main()

