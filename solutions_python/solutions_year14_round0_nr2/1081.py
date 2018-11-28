content = open("B-large.in", "r").read().split("\n")
inputs = int(content[0])
output = open("cookiesoutput.txt", "w")
for i in range(1, inputs+1):
	timeUsed = 0
	cookieRate = 2
	cookies = 0
	C, F, X = content[i].split(" ")
	C = float(C)
	F = float(F)
	X = float(X)
	while(cookies < X):
		if (X/cookieRate) < ((X/(cookieRate+F))+(C/cookieRate)):
			timeUsed += X/cookieRate
			cookies = X
			output.write("Case #{0}: {1}\n".format(i, timeUsed))
		else:
			timeUsed += C/cookieRate
			cookieRate += F
			
	
	
