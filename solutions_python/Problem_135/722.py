import sys
def process(case,index,res,first) :
	global answer
	tmp = []
	card = []
	result = ""
	for data in res[index]:
		tmp.append(data)
	if first == True:
		answer = tmp
		index1 = index
	else:
		for i in range(4):
			if tmp[i] in answer:
				card.append(tmp[i])
		if len(card) == 1:
			result = str(card[0])
		elif len(card) == 0:
			result = "Volunteer cheated!"
		else:
			result = "Bad magician!"
		print "Case #%d: %s" % (case, result)

f = open(sys.argv[1])
n = int(f.readline())
first = True
for i in range(n*2) :
	index = int(f.readline())
	lst = []
	for j in range(4) :
		lst.append(f.readline().split())
	process(i/2+1,index-1,lst,first)
	first = not first
