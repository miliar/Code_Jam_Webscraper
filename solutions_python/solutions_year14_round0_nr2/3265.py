f = [i for i in open('B-large.in')]
f[-1] +='\n'
data = [i[:-1] for i in f]
cases = []
for i in range(int(data[0])):
	data1 = data[i+1].split(' ')
	time = 0
	inc = 2
	farm = float(data1[0])
	farminc = float(data1[1])
	goal = float(data1[2])
	f = True
	while f:
		if goal/inc> farm/inc + goal/(inc+farminc):
			time += farm/inc
			inc +=farminc
		else:
			time += goal/inc
			f = False
	cases.append('Case #'+str(i+1)+': '+ "%.7f" %time )

# print(cases)
f1 = open('output.txt','w')
[f1.write(i+'\n') for i in cases]