import math

infile = open("C-small-attempt0.in","r")
outfile = open("output.txt","w")
lines = infile.readlines()

params = lines[0].rstrip()

for i in range(0,int(params)):
	count = 0
	intval = [int(item) for item in lines[i+1].rstrip().split()]
	start = int(math.ceil(math.sqrt(intval[0])))
	end = int(math.floor(math.sqrt(intval[1])))
	for j in range(start,end+1):
		if(str(j*j) == str(j*j)[::-1] and str(j) == str(j)[::-1]):
			count = count + 1

	# output result to file
	outfile.writelines("Case #"+str(i+1)+": "+str(count)+"\n")

infile.close()
outfile.close()
