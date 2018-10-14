inp = open("A-large.in.txt", "r")
testcase=int(inp.readline())
# print testcase
input = [0]*4

case=0
out = open("./out.txt", "w")

for x in xrange(testcase):
	case+=1
	result=0
	temp=inp.readline().split()
	top=int(temp[0])
	audience=temp[1]

	clapping=0
	for i in xrange(top+1):
		if clapping < i:
			result+=i-clapping
			clapping=i
		clapping+=int(audience[i])

	out.write("Case #"+str(case)+": "+str(result)+"\n")

out.close()

