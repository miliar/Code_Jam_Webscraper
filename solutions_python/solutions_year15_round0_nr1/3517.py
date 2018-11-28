def process_case(maxval, numarray):
	peopletoadd = 0
	if maxval == 0:
		return 0
	for i in range(len(numarray)):
		if int(numarray[i]) == 0:
			if i +1 < len(numarray):
				if int(numarray[i+1]) !=0:
					peopletoadd += 1
				else:
					for j in range(i,len(numarray)):
						if numarray[j] >0:
							peopletoadd +=1
							break
	return peopletoadd


def process_case2(maxval, numarray):
	peopletoadd = 0
	totalpeople = 0
	if maxval == 0:
		return 0
	for i in range(len(numarray)):
		if totalpeople < i:
			diff =  i - totalpeople
			peopletoadd = peopletoadd + diff
			totalpeople = totalpeople + diff
		totalpeople = totalpeople + int(numarray[i])

	return peopletoadd











f = open('A-small-attempt2.in', 'r')
num = int(f.readline())
endarray = []

for x in range(0,num):
	vals = f.readline()
	vals = vals.rstrip('\n')
	mx = vals[0]
	mx = int(mx)
	nums = vals[2:]
	print  "Case #" + str(x+1) + ": " + str(process_case2(mx,nums))








#Output 

#Case #1: 0
#Case #2: 1
#Case #3: 2
#Case #4: 0

