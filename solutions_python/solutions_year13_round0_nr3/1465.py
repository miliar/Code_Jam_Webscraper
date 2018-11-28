import math
input = open('C-small-attempt1.in', 'r')
input.readline()
count = 0
output = open("output.txt", 'w')
for line in input:
	count+=1
	bounds = line.split(" ")
	lower2 = math.sqrt(float(bounds[0]))
	lower = int(lower2)
	if(lower2%1!=0.0): lower+=1
	upper = int(math.sqrt(float(bounds[1])))
	fsqcount = 0
	while(lower <= upper):
		test = lower**2
		if((str(test) == str(test)[::-1]) and (str(lower) == str(lower)[::-1])): fsqcount += 1
		lower+= 1
	output.write("Case #" + str(count) + ": " + str(fsqcount) + "\n") 
input.close()
output.close()
