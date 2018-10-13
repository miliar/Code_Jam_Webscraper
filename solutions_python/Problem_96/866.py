
def summa(mylist):
	res = int(mylist[0])+ int(mylist[2])+ int(mylist[1])
	#print(summa, mylist, res)
	return res

def generate(score, describe):
	mylist1 = []
	mylist2 = []

	down = int(score/3)-2
	up = int(score/3)+3

	if down < 0:
		down = 0

	#print down, up, score
	
	for i in xrange(down, up):
		for j in xrange(i, up):
			for k in xrange(j, up):
				testlist = [i, j, k]
				#print testlist, score
				if summa(testlist) == score:
					if testlist[2] - testlist[0] < 2:
						if testlist[2] >= describe:
							mylist1.append(testlist)
					else:
						if testlist[2] - testlist[0] < 3:
							if testlist[2] >= describe:
								mylist2.append(testlist) 

	return mylist1, mylist2

def funct(googlers, surprising, describe, scores):
	#print(googlers, surprising, describe, scores)
	res = 0
	for score_str in scores:
		scr = int(score_str)
		mylist1, mylist2 = generate(scr, describe)
		#print(mylist1, mylist2)
		if len(mylist1)>0:
			res +=1
		else:
			if(len(mylist2)>0 and surprising>0):
				surprising -= 1
				res += 1
	return res



T = input()

# print summa([-1,0,1]) == 1
# ll = generate(13, 5)
# print ll
# ll = generate(11, 5)
# print ll
# ll = generate(15, 5)
# print ll

for i in xrange(0, T):
	data = raw_input()
	nabor = data.split(' ')
	googlers_count = int(nabor[0])
	surprising = int(nabor[1])
	describe = int(nabor[2])
	scores = nabor[3:]
	# print 'goog-s', googlers_count 
	# print 'surprising', surprising 
	# print 'describe', describe 
	# print 'scores', scores 	

	res = funct(googlers_count, surprising, describe, scores)

	print 'Case #%(iteration)i: %(result)i'%{'iteration':i+1, 'result':res}