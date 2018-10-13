infile = open('infile.in','r');
outfile = open('outfile.out','w');
lines = int(infile.readline());
line = ''
buttons = 0
linepos = 1
OPos = 1
ONext = 0
BPos = 1
BNext = 0
seconds = 0;
NextB = '';
tmp = '';
tmp2 = ''
tmpint = 2;
buttonpush = False

for i in range (lines):
	tmp2 = ''
	tmp = infile.read(1)
	while(tmp2 != ' '):
		tmp2 = infile.read(1)
		if(tmp2 != ' '):
			tmp = tmp + tmp2
	
	buttons = int(tmp)

	line = infile.readline()
	seconds = 0
	linepos = 0
	for i2 in range (buttons):

		NextB = line[linepos]
		tmpint = 2
		tmp = ''
		for i3 in range (linepos, len(line)-1):
			if(line[i3] == 'O' and ONext == 0):
				while(line[i3+tmpint] != " " and line[i3+tmpint] != "\n"):
					tmp = tmp + line[i3+tmpint]
					tmpint = tmpint + 1
				ONext = int(tmp)
				break;			
		
		tmpint = 2
		tmp = ''
		for i3 in range (linepos, len(line)-1):		
			if(line[i3] == 'B' and BNext == 0):
				while(line[i3+tmpint] != " " and line[i3+tmpint] != "\n"):
					tmp = tmp + line[i3+tmpint]
					tmpint = tmpint + 1	
				BNext = int(tmp)
				break;

		linepos = linepos + 1
		tmp = ''
		while(tmp != 'B' and tmp != 'O' and linepos < len(line)-1):
			tmp = line[linepos]
			if(tmp != 'B' and tmp != 'O' and linepos < len(line)-1):
				linepos = linepos+1 
		

		while(True):			

			if(OPos == ONext and NextB == 'O'):
				ONext = 0
				buttonpush = True
			else:
				if(OPos < ONext):
					OPos = OPos + 1
				else:
					if(OPos > ONext):
						OPos = OPos - 1
					


			if(BPos == BNext and NextB == 'B'):		
				BNext = 0
				buttonpush = True
			else:
				if(BPos < BNext):
					BPos = BPos + 1		
				else:
					if(BPos > BNext):
						BPos = BPos - 1


			seconds = seconds + 1
			if(buttonpush == True):
				buttonpush = False
				break			


		
	ONext = 0;
	BNext = 0;
	OPos = 1;
	BPos = 1;	
	
	outfile.write('Case #'+str(i+1)+': '+str(seconds)+'\n')
		
infile.close();
outfile.close();

