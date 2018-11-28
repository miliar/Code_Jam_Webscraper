t = open("B-small-attempt1.in","r")
out = open("output.txt","w")
s = int(t.readline())
f = 0
w=""
for i in range(0,s):
	w =t.readline()
	x = int(w);
	#print(w,len(w)-1,w[len(w)-2])
	while(x > 0):
		f=0
		for j in range(0,len(str(x))-1):
			if int(w[j])-int(w[j+1]) > 0:
				f=1
				break	
		if f==1:	
			x-=1
			w = str(x)		
		if f==0:
			out.write('Case #%d: %d\n'%(i+1,x))
			#print(x)
			break;
	 	
