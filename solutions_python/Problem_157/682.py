inp = open("C-small-attempt1.in.txt", "r")
testcase=int(inp.readline())
# print testcase
input = [0]*4

case=0
out = open("./out.txt", "w")


def calc(inpString):
	if len(inpString)==1:
		return ""
	if len(inpString)>1:
		x=inpString[0]
		y=inpString[1]
		rev=False
		if x=="i":
			if y=="i":
				head=""
				rev=True
			elif y=="j":
				head="k"
			elif y=="k":
				head="j"
				rev=True

		elif x=="j":
			if y=="i":
				head="k"
				rev=True

			elif y=="j":
				head=""
				rev=True
			elif y=="k":
				head="i"

		elif x=="k":
			if y=="i":
				head="j"
			elif y=="j":
				head="i"
				rev=True
			elif y=="k":
				head=""
				rev=True

		return (head+inpString[2:], rev)

for x in xrange(testcase):
	case+=1
	print ">>>CASE",case
	
	temp=inp.readline().split()
	# print temp
	times=int(temp[1])

	temp=inp.readline()
	inputString=(temp.strip())*times

	
	print inputString

	sign="+"

	i, j, k=False, False, False

	result="No"

	while(len(inputString)>=3 and i==False):
		if inputString[0]=="i" and sign=="+":
			i=True
			inputString=inputString[1:]
			print "!!! i done"
		else:
			inputString, rev=calc(inputString)
			if rev==True:
				if sign=="+":
					sign="-"
				elif sign=="-":
					sign="+"
			# print sign+inputString

	while(len(inputString)>=2 and i==True and j==False):
		if inputString[0]=="j" and sign=="+":
			j=True
			inputString=inputString[1:]
			print "!!! j done"
			print inputString
		else:
			inputString, rev=calc(inputString)
			if rev==True:
				if sign=="+":
					sign="-"
				elif sign=="-":
					sign="+"
		# print sign+inputString

	while(len(inputString)>1 and j==True):

		inputString, rev=calc(inputString)
		if rev==True:
			if sign=="+":
				sign="-"
			elif sign=="-":
				sign="+"
		print sign+inputString

	if inputString=="k" and sign=="+":
		k=True
		result= "YES"

	# print result
	
	out.write("Case #"+str(case)+": "+str(result)+"\n")

out.close()

