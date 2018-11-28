inp = open("D-small-attempt2.in.txt", "r")
testcase=int(inp.readline())
# print testcase
input = [0]*4

case=0
out = open("./out.txt", "w")

for x in xrange(testcase):
	case+=1
	
	temp=inp.readline().split()
	x=int(temp[0])
	r=int(temp[1])
	c=int(temp[2])

	if (r*c)%x!=0:
		result="RICHARD"
	else:
		if x==4 and min(r, c)==2:
			result="RICHARD"
		else:
			if x%2==1:
				edge=(x+1)/2
			else:
				edge=x/2
			# print edge, min(r,c)

			if edge>min(r,c) or x>max(r, c):
				result="RICHARD"
			else:
				result="GABRIEL"


	# print result
	
	out.write("Case #"+str(case)+": "+str(result)+"\n")

out.close()

