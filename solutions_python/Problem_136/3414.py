filein = open("B-small-attempt0.in","r")
fileout = open("out.out","w")
line = filein.readline()
T=int(line)
for t in range(T):
	line = filein.readline()
	splitter = line.split(" ")
	C = 0.0
	F = 0.0
	X = 0.0 
		#aixo es per forzar el tipus "DOUBLE"
		#ja que necessitem 6 decimals de precisio
	C = float(splitter[0])
	F = float(splitter[1])
	X = float(splitter[2])
	
	cookies = 0.0
	cookiesXsec = 2.0
	time = 0.0
	tempsRecord = 666666666 #el maxim
	
	maximGranges = 0
	while maximGranges < X and time <= tempsRecord:
		cookies = 0.0
		granges = 0
		time = 0.0
		cookiesXsec = 2
		while cookies < X:
			cookies += cookiesXsec
			time+=1
			if granges < maximGranges and cookies+cookiesXsec >= C:
				time += (C-cookies) / cookiesXsec
				cookies = 0.0
				cookiesXsec += F
				granges += 1
			
		cookies -= X
		if cookies > 0:
			time -= 1
			time += (cookiesXsec - cookies) / cookiesXsec
		if time < tempsRecord:
			tempsRecord = time	
		maximGranges+=1
	fileout.write("Case #"+str(t+1)+": "+str(tempsRecord)+"\n")
filein.close()
fileout.close()
