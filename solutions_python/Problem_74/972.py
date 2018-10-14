import sys;
def main():
	filename = sys.argv[1]
	f=open(filename,'r')
	outf=open("output.txt", 'w')
	numtests = int(f.readline())
	total = numtests
	while numtests > 0:
		input=str.split(f.readline())
		numtests = numtests - 1
		totmoves = int(input.pop(0))
		t = 0
		opos = 1
		bpos = 1
		otime = 0
		btime = 0
		i=0
		while i < totmoves:
			i = i+1
			robot = input.pop(0)
			nextpos = int(input.pop(0))
			if robot == 'O':
				timetoreach = abs(nextpos-opos)
				timeelapsed = t-otime
				if timetoreach <= timeelapsed:
					t=t+1
				else:
					t=t+1+timetoreach - timeelapsed
				opos = nextpos
				otime = t
			else:
				timetoreach = abs(nextpos-bpos)
				timeelapsed = t-btime
				if timetoreach <= timeelapsed:
					t=t+1
				else:
					t=t+1+timetoreach - timeelapsed
				bpos = nextpos
				btime = t
		outf.write('Case #'+str(total-numtests)+': '+str(t)+'\n')	
		print ('Case #',total-numtests,': ',t)
		
	f.close()
	outf.close()

main()
	
		