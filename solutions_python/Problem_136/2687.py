

# inputfile = "B-small-attempt1.in"
# inputfile = "2-small-input.in"
inputfile = "B-large.in"
outfile = inputfile.split(".")[0]+".out"


fin = open(inputfile,'r')
fout = open(outfile,'w')
testcases = int(fin.readline())


for casenum in range(1,testcases+1):

	c,f,x = map(float,fin.readline().split())
	# print c,f,x
	costToNewFarm = 0
	costs = []
	rate = 2.0
	while True:
		costs.append(costToNewFarm+x/rate)

		
		costToNewFarm+= c/rate
		# print 'rate = ',rate,',costs to finish=',costs[-1],',costToNewFarm=',costToNewFarm
		rate += f
		# if not(rate <= x):
		# 	break
		if len(costs)>1:
			if costs[-1] > costs[-2]:
				break

	# print ("Case #%d: %.7f"%(casenum,min(costs)))
	fout.write("Case #%d: %.7f\n"%(casenum,min(costs)))

	# break


