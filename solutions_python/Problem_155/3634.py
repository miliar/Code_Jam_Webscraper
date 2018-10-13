f=file("A-small-attempt0.in","r")
f=f.read()
f=f.split("\n")
t=int(f[0])
f2=file("ans.txt","w")
for i in range(t):
	q=f[i+1].split(" ")[1]
	count=0
	ans=0
	#print "))))))))))"
	for mm in range(len(q)):
		if count<mm:
			ans+=mm-count;	
			count+=(mm-count)	
		count+=int(q[mm])
		#print count
	f2.write("Case #"+str(i+1)+": "+str(ans)+"\n")
f2.close()
				
	
