

inp=open("input.txt", 'r')

tests =int(inp.readline())

for i in range(tests):
	first = int(inp.readline())
	for j in range(first):
		line = inp.readline()
	for j in range(4-first):
		trash=inp.readline()
	line = line.split(' ')
	second = int (inp.readline())
	for j in range(second):
		sline = inp.readline()
	for j in range(4-second):
		inp.readline()
	sline = sline.split(' ')
	answer=-1
	for k in line:
		for j in sline:
			if k.strip()==j.strip() and answer==-1:
				answer = k.strip()
			elif k.strip()==j.strip() and answer!=-1:
				print("Case #", i+1,  ": Bad magician!", sep="")
				answer = -2
				break
		if answer==-2:
			break
	if answer==-1:
		print("Case #", i+1, ": Volunteer cheated!", sep="")
	elif answer != -2:
		print("Case #", i+1, ": ", answer,sep="")

				
