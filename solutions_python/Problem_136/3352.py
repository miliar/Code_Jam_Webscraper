f = open("B-small-attempt0.in","r")
numberOfCases = f.readline()
fw = open("data2-output.txt","w")
for i in range(int(numberOfCases)):
	line = f.readline()
	C,F,X = line.split(" ")
	C,F,X = float(C),float(F),float(X)
	time1 = X/2
	time2 = C/2 + X/(F+2)
	cookies = 2
	while time1 > time2:
		cookies = cookies + F
		time1 = time2
		time2 = time2 - X/cookies + C/cookies + X/(F+cookies)
	if time1 > time2:
		fw.write("Case #"+str(i+1)+": "+str(time2)+"\n")
	else:
		fw.write("Case #"+str(i+1)+": "+str(time1)+"\n")
