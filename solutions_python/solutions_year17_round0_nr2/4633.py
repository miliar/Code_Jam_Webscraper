T=int(input())
file = open("output_of_tidy.txt","w")
for z in range(0,T):
	n=int(input())
	while(n>0):
		k=list(map(int,list(str(n))))
		l=sorted(map(int,list(str(n))))

		if k==l:
			file.write("Case #"+str(z+1)+": "+str(n))
			file.write("\n")
			break
		n-=1
file.close()