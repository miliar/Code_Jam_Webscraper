infile = open('file.in','r')
outfile = open('out.txt','w')
t = int(infile.readline())
for i in range(t):
	line = infile.readline().split()
	aud = line[1]
	app = int(aud[0])
	friends = 0
	for j in range(1,int(line[0])+1):		
		if app<j:
			friends+=j-app
			app=j
		app+=int(aud[j])
	outfile.write("Case #"+str(i+1)+": "+str(friends) + "\n")
	
		
