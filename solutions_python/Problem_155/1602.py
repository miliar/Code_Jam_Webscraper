import sys

inputfile = open('A-large.in')
outputfile = open('A-large.out','w')
T = inputfile.readline()
for x in range(int(T)):
	data = inputfile.readline()
	data = data.split()
	minshy = int(data[0])
	shy = data[1]
	count = int(shy[0])
	ans = 0
	for i in range(1,minshy+1):
		need = i
		if shy[i] == 0:
			continue
		if count < need:
			ans = ans + (need-count)
			count = need
		
		count = count + int(shy[i])
	outputfile.write("Case #"+str(x+1)+": "+str(ans)+"\n")
inputfile.close()
outputfile.close()