a=int(input())
li=[]
for i in range(a):
	b=input()
	for j in range(int(b),0,-1):
		#print(j)
		if str(j)==''.join(sorted(str(j))):
			print("Case #",i+1,": ",j,sep="")
			break
	
	