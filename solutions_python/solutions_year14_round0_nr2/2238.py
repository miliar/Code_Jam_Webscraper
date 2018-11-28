def readfile():
	with open('input.in', 'r') as f:
		data = f.readlines()
		numTest = int(data[0])
		print numTest
		w = open('output.ou','w')
		for i in range(numTest):
			input = data[i+1]
			rs = analyze(input)
			pos = i + 1
			r = "Case #"+str(pos) + " "
			rs = "{:.7f}".format(rs)
			r = r + rs +"\n"
			w.write(r)
			print r
			print "======================"
		w.close()
	return 1
def analyze(input):
	input = input.split()
	print input
	c= float(input[0])
	f = float(input[1])
	x = float(input[2])
	numFarm = 0
	numCookieGetBySecond = 2
	remainCookies = x
	numCookie = 0
	time = 0
	i = 0
	while True:
		timeGetFarm = c / numCookieGetBySecond
		t = numCookieGetBySecond + f
		timeIfGetMoreFarm = (x / t) + timeGetFarm
		timeFinish = x / numCookieGetBySecond
		if timeFinish < timeIfGetMoreFarm:
			time = time + timeFinish
			break
		else:
			time = time + timeGetFarm
			numFarm = numFarm + 1
			numCookieGetBySecond = numCookieGetBySecond + f
		i = i + 1

	return time
if __name__ == "__main__":
	print readfile()