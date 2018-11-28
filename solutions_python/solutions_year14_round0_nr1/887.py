inp = open("A-small-attempt0.in", "r")
testcase=int(inp.readline())
# print testcase
input = [0]*4
temp=0
case=0
out = open("./out.txt", "w")

for x in xrange(testcase):
	case+=1
	answer1=int(inp.readline())
	for i in xrange(0,4):
		input[i]=[int(temp) for temp in (inp.readline()).split(" ")]
	numRange1=input[answer1-1]

	answer2=int(inp.readline())
	for i in xrange(0,4):
		input[i]=[int(temp) for temp in (inp.readline()).split(" ")]
	numRange2=input[answer2-1]

	# print numRange1, numRange2
	replica=0
	for a in numRange1:
		if a in numRange2:
			replica+=1
			card=a

	if replica==1:
		out.write("Case #"+str(case)+": "+str(card)+"\n")
	elif replica==0:
		out.write("Case #"+str(case)+": Volunteer cheated!"+"\n")
	elif replica>1:
		out.write("Case #"+str(case)+": Bad magician!"+"\n")

out.close()

