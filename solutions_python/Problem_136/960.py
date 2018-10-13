f = open('B-large.in.txt','r')
text_file = open("Output2.txt", "w")
numberOfCase = int(f.readline())

for x in xrange(0,numberOfCase):
	inputs = f.readline()
	inputs = inputs.strip()
	alist = inputs.split(' ')
	
	C = float(alist[0])
	F = float(alist[1])
	X = float(alist[2])

	productionRate = 2
	additionalproductionRate = 0
	totalTime = 0
	while(True):

		timeNeed = X / productionRate


		if (timeNeed <= C/productionRate + X/(F+productionRate)):
			totalTime += timeNeed
			break
		else:
			totalTime += C/productionRate
			productionRate += F


		

	text_file.write("Case #"+str(x+1)+": "+str(round(totalTime,7))+"\n")

text_file.close()

	