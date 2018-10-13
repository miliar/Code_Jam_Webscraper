testCases = input()

aux = []

for i in range(testCases):
	line = raw_input()
	line = line.split(" ")
	c = float(line[0])
	f = float(line[1])
	x = float(line[2])
	
	cookieRate = 2
	seconds = 0
	
	while( (x/cookieRate) >  (( c/cookieRate ) + (x/(cookieRate+f))) ):
		seconds = seconds + ( c/cookieRate )
		cookieRate = cookieRate + f
		
	seconds = seconds + (x/cookieRate)
	aux.append(seconds)

counter = 0
for i in aux:
	counter = counter + 1
	print "Case #" + str(counter) + ": " + str(i) 
	
