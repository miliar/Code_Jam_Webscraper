myfile = open("A-large.in", "r")
myfile2 = open("output.txt", "w")

case = 0
testcase = int(myfile.readline())
h_dist = []
h_spd = []
hours = []

while True:
	
	line = myfile.readline()
	if not line: 
		break
	
	

	myline = line.split(" ")

	h_dist = []
	h_spd = []
	hours = []
	distance = float(myline[0])
	horse_num = int(myline[1])
	num = horse_num
	case+=1


	for a in range(num):
		line = myfile.readline()
		myline = line.split(" ")

		h_dist.append(float(myline[0]))
		h_spd.append(float(myline[1]))
	
	for x in range(len(h_dist)):
		temphour = (distance-h_dist[x])/h_spd[x]
		hours.append(temphour)
	ans = distance/max(hours)


	if case != 1:
		myfile2.write("\n")		
	
	
	myfile2.write("Case #")
	myfile2.write(str(case))
	myfile2.write(": ")
	myfile2.write(str('{0:.6f}'.format(ans)))


