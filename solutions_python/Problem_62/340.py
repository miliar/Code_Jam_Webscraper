
fread=open('C:\Users\Sandip\Desktop\A3.in','r')
fwrite=open('C:\Users\Sandip\Desktop\FINAL2.out','w')


total_cases=fread.readline().strip()
for i in range(int(total_cases)):
	N = int(fread.readline().strip())
	A=[]
	B=[]
	for n in range(N):
		AB = fread.readline().strip().split(" ")
		A.append(int(AB[0] ))
		B.append( int(AB[1]))
	
	count=0
	for j in range(N):
		for k in range(1,N-j):
			#print "A[j]",A[j] , " A[k] " , A[k]
			#print "B[j]",B[j], "  B[k]",B[k]
			if A[j] > A[k] :
				if B[j]< B[k]:
					count = count + 1
			else:
				
				if B[j] > B[k] :
					count = count +1
	fwrite.write("Case #" + str(i+1) + ": " + str(count) + "\n")
		
fread.close()
fwrite.close()


