import sys

sfin=sys.argv[1]
if len(sys.argv)<2:
	sfout=sys.argv[2]
else:
	sfout=sfin+".out"

fin=open(sfin,'r')
fout=open(sfout,'w')
outputFormat='Case #{0}: {1}\n'

##Programa

def GetNextButton(robot):
	try:
		x = case.index(robot)
		x=case[x+1]
		return x
	except ValueError:
		return None

def RemoveCase(robot):
	try:
		x = case.index(robot)
		case.pop(x)
		x=case.pop(x)
		return x
	except ValueError:
		return None



tcases = fin.readline()
icase=1
while int(icase)<=int(tcases):
	case = fin.readline().replace("\n","").split(' ')
	buttons=case.pop(0)

	opos=1
	bpos=1
	orange=GetNextButton('O')
	blue=GetNextButton('B')
	i=0
	time=0
	while i<int(buttons):
		aux=case[0]
		if orange is not None:
			if int(orange) == int(opos):
				if aux=='O':
					#push button
					case.pop(0)
					case.pop(0)
					orange=GetNextButton('O')
					i=i+1
			else:
				dif=int(orange) - int(opos)
				opos = opos + ( dif / abs(dif) )
					
		
		if blue is not None:
			if int(blue) == int(bpos):
				if aux=='B':
					#push button
					case.pop(0)
					case.pop(0)
					blue=GetNextButton('B')
					i=i+1
			else:
				dif=int(blue) - int(bpos)
				bpos = bpos + int( dif / abs(dif) )
		
		time=time+1
		
	print time
	if int(icase)==int(tcases):
		fout.write(outputFormat.format(icase,time).replace("\n",""))
	else:
		fout.write(outputFormat.format(icase,time))
	icase=icase+1

##fin programa
fin.close()	
fout.close()