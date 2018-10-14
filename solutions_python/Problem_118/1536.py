fileIn = open("C-large-1.in","r")
fileOut = open("C-large-1.out","w")
lines = fileIn.readlines()
fileIn.close()
cases = int(lines[0])

fnsn=[0, 1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004,1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004]

k=1

for t in range(0,cases):
	count=0
	thres1,thres2 = lines[k].split()
	for i in fnsn:
		if i>=int(thres1) and i<=int(thres2):
			count+=1
		if i > thres2:
			break
	fileOut.write("Case #"+str(t+1)+": "+str(count)+"\n")		
	k+=1
fileOut.close()
