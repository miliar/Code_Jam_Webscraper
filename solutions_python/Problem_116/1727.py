import re

input = open('c:\\users\\snuff\\desktop\\codeJam\\A-large.in','r+')
output = open('c:\\users\\snuff\\desktop\\codeJam\\a-large.out','w+')

cases = int(input.readline())

x = re.compile(r'.*[XT][XT][XT][XT]')
o = re.compile(r'.*[OT][OT][OT][OT]')
dot = re.compile(r'.*\.')

result = ""

for case in range(0, cases):
	hor = ""
	ver = ""
	dia = ""
	line1 = input.readline().rstrip()
	line2 = input.readline().rstrip()
	line3 = input.readline().rstrip()
	line4 = input.readline().rstrip()
	input.readline()
	
	hor = line1 + " " + line2 + " " + line3 + " " + line4 + " " 
	
	for i in range(4):
		ver += line1[i] + line2[i] + line3[i] + line4[i] + " "
	dia=line1[0] + line2[1] + line3[2] + line4[3] + " " + line1[3] + line2[2] + line3[1] + line4[0]
	inLine = hor + ver + dia
	
	if(x.match(inLine)!=None):
		result = "X won"
		print("Case #"+str(case+1)+": " + result, file=output)
		continue
	elif(o.match(inLine)!=None):
		result = "O won"
		print("Case #"+str(case+1)+": " + result, file=output)
		continue
	elif(dot.match(inLine)!=None):
		result = "Game has not completed"
		print("Case #"+str(case+1)+": " + result, file=output)
		continue
	else:
		result = "Draw"
		print("Case #"+str(case+1)+": " + result, file=output)
		continue

	
	
	
	