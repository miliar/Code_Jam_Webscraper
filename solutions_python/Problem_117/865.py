def checkge(a, array):
	res = 1
	for i in range(len(array)):
		if(a < array[i]):
			res = 0
			break
	return res


infile = open("B-large.in","r")
outfile = open("output.txt","w")
lines = infile.readlines()

params = lines[0].rstrip()

n = 0
m = 0
index = 0
for i in range(0,int(params)):
	grass = []
	goodpattern = 1
	nm = lines[1+index].rstrip().split()
	n = int(nm[0])
	m = int(nm[1])

	# get matrix
	for j in range(n):
		grass.append([int(item) for item in lines[2+index+j].rstrip().split()])
	grassT = [[r[col] for r in grass] for col in range(len(grass[0]))]

	# check the grass pattern
	for j in range(n):
		for k in range(m):
			# check if the number is bigger or equal to all others in its line or column
			res = checkge(grass[j][k], grass[j])
			resT = checkge(grass[j][k], grassT[k])
			if(res==0 and resT==0):
				goodpattern=0
				break

	index = index+n+1
	# output result to file
	if(goodpattern == 1):	
		outfile.writelines("Case #"+str(i+1)+": YES\n")
	else:
		outfile.writelines("Case #"+str(i+1)+": NO\n")

infile.close()
outfile.close()
