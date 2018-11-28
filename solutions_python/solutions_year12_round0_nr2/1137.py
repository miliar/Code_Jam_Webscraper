prtdir = '/home/rajkumar/google-codejam/Dance/'
input = open(prtdir+ 'input.txt','r')
output = open(prtdir+'output.txt','w')

testcases = int(input.readline())


for i in range(testcases):
	scores=[]
	noofhighscores = 0
	slist = input.readline().rstrip().split(' ')
	ilist = [int(v) for v in slist]
	for j in range(ilist[0]):
		score = ilist[3+j]
		if score == 0:
			scores.append([score,score])
		elif score%3 == 0:
			scores.append([score/3,(score/3)+1])
		elif (score+1)%3 == 0:
			scores.append([(score+1)/3,((score+1)/3)+1])
		elif (score+2)%3 == 0:
			scores.append([(score+2)/3,(score+2)/3])
	
	print scores
	surprise = ilist[1]
	print surprise
	p = ilist[2]
	print p
	for e in scores:
		lst = e
		if lst[0] >= p:
			noofhighscores = noofhighscores + 1
		elif lst[1] >= p:
			if surprise != 0:
				surprise = surprise -1 
				noofhighscores = noofhighscores + 1
	print noofhighscores
	output.write('Case #'+ str(i+1) +': '+str(noofhighscores)+'\r\n')

output.close()
		
			