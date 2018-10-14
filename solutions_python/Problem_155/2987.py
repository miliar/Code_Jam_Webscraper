inputs=[]
with open("A-large.in") as f:
    for line in f:
        inputs.append(line);
t=int(inputs[0])
for i in range(0,t):
	s=inputs[i+1];
	smax=int(s.split(" ")[0])
	sarr=list(s.split(" ")[1])
	nsh=int(sarr[0])
	req=0
	required=0
	for j in range(1,len(sarr)-1):
		if(int(sarr[j])>0):
			if(nsh>=j):
				nsh+=int(sarr[j]);
			else:
				req=j-nsh
				nsh+=req
				nsh+=int(sarr[j])
				required+=req
	f = open('output.txt','a');
	f.write("Case #"+str(i+1)+": "+str(required)+"\n");
	f.close();
