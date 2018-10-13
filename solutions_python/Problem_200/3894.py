import sys
f = open('out17b.out','w')
T = int( sys.stdin.readline().strip())
case=0

def InOrder( _S):
	tehIn = range(len(_S)-1)
	return all(_S[i] <= _S[i+1] for i in tehIn)

while( T>0 ):
	T-=1
	case+=1

	Nstr = sys.stdin.readline().strip()
	Nint= int (Nstr)
	NintTEST= int (Nstr)
	# print(Nint)
	count = 0
	# countTEST = 0


	while NintTEST >0:
		testTEST = str(NintTEST)
		# print(InOrder(testTEST))
		if  InOrder(testTEST):
			# print(testTEST)
			respTEST = testTEST
			break
		NintTEST -=1
	if len(Nstr)>2:
		while Nstr[count]<= Nstr[count+1]:
			if count== len(Nstr)-3:
				break
			count +=1
		# print("tiene: ",count)
		realIntSearch = int(Nstr[count:len(Nstr)])
		lenOrderPArt= len(Nstr[count:len(Nstr)])
		# print(realIntSearch)
		# print(lenOrderPArt)
		while realIntSearch >0:
			test = str(realIntSearch)
			# print(InOrder(test))
			if  InOrder(test):
				# print(test)
				resp = test
				break
			realIntSearch -=1
		# print(Nstr[0])
		# print(resp)
		# print(count)
		if count >1:
			prefix = int(Nstr[0:count])
			if len(resp)<lenOrderPArt:
				prefix = int(Nstr[0:count+1])-(int(Nstr[0:count]) +1)
			# print(prefix,resp)
			resp =str(prefix)+resp
	else:
		while Nint >0:
			test= str(Nint)
			# print(InOrder(testTEST))
			if  InOrder(test):
				# print(test)
				resp = test
				break
			Nint-=1
		# resp = Nstr
	if resp != respTEST:
		print("WARNIGN entrada", Nstr, " obtuve ", resp, " esperaba ", respTEST)
	# print    ("Case #"+str(case)+": "+str(resp))
	f.write ("Case #"+str(case)+": "+str(resp)+"\n")
	# break
f.close();
