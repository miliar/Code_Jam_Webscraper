from sets import Set
n = int(raw_input());
f= open("temp.txt","w")
for z in range(1,n+1):
	m = int(raw_input());
	for i in range(1,5):
		k = raw_input();
		if(i==m):
			k = k.split(" ");
			mat1 = Set(k);
	m = int(raw_input());
	for i in range(1,5):
		k = raw_input();
		if(i==m):
			k = k.split(" ");
			mat2 = Set(k);
	common = mat1.intersection(mat2);		
	if(len(common) == 1):
		for x in common:
			f.write("Case #"+str(z)+": "+str(x)+"\n");
	elif (len(common) > 1):
		f.write("Case #"+str(z)+": Bad magician!"+"\n");
	elif (len(common) == 0):
		f.write("Case #"+str(z)+": Volunteer cheated!"+"\n");
f.close()
		
