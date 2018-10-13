file = open("newfile.txt", "w")
file1 = open("B-large.in.txt","r")
data = file1.readlines()
T=int(data[0])
for i in range (1,T+1):
	
	data1=data[i].split()
	time=0.0
	rate=2.0
	C=float(data1[0])
	F=float(data1[1])
	X=float(data1[2])
	while ((X/rate) > ((X)/(rate+F))+(C/rate)):
		time=time+(C/rate)
		rate=rate+F
	time+=X/rate
	file.write("Case #%d: %f\n"% (i,time))
	
	
file1.close()
file.close()