fr = open("in.txt", "r")
fw = open("out.txt", "w")
T = int(fr.readline())
for i in range(T):
	fw.write("Case #" + str(i+1) + ": ")
	line = fr.readline()
	inputlst = line.split(" ")
	lst = [float(x) for x in inputlst]
	c = lst[0]
	f = lst[1]
	x = lst[2]
	farms = 0.0
	cookies = 0.0
	t = 0.0
	rate = 2.0
	while cookies < x:
		if x - cookies <= c:
			ans = t + (x - cookies) / rate
			cookies = x
		elif (x - cookies) / rate <= (x - cookies) / (rate + f) + c/rate:
			ans = t + (x - cookies) / rate
			cookies = x
		else:
			t = t + c / rate
			rate = rate + f
	fw.write(str(ans) + "\n")
