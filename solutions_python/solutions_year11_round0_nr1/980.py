filename = "A-small-attempt0"
f = open(filename+".in")
num_testcases = f.readline()
num_buttons = [0]
lines = []
queue = []
time = 0

Bloc = [0]
Oloc = [0]

Block = [0]
Olock = [0]

Bdone = [0]
Odone = [0]

pressed = [0]

Bindex = [0]
Oindex = [0]

Btarget = [-1]
Otarget = [-1]

Bnext = [0] # -1 = advance left  0 = wait, 1= advance right , 2 press button
Onext = [0] # -1 = advance left  0 = wait, 1= advance right , 2 press button

Bwait = [0]
Owait = [0]

turn = ['N']
turnIndex = [0]

for line in f:
	lines.append(line[:-1])


def B_calculate_next_action():
	if( Bdone[0] == 1 ):
		return
	
	if( num_buttons[0] == 0 ):
		Bdone[0] = 1
		return

	if( Bwait[0] == 1 ):
		if( Bloc[0] == Btarget[0] ):
			Bwait[0] = 1
			Bnext[0] = 2
		else:
			Bnext[0] = 0
		return
	
	if( Block[0] == 0 ):
		for i in range( Bindex[0], len(queue) ):
			if i == ( len(queue) -1 ):
				Bdone[0] = 1
				break
			if queue[i] == 'B' :
				Btarget[0] = int(queue[i+1])
				Bindex[0] = i + 1
				Block[0] = 1
				break
	if (  Btarget[0]<0 ):
		Bdone[0] = 1
		return

	if( Bloc[0] == Btarget[0] ):
		Bwait[0] = 1
		Bnext[0] = 2
		return
		
	if( Bloc[0] < Btarget[0] ):
		Bwait[0] = 0
		Bnext[0] = 1
		return

	else:
		Bwait[0] = 0
		Bnext[0] = -1
		return

def O_calculate_next_action():
	if( Odone[0] == 1 ):
		return
	
	if( num_buttons[0] == 0 ):
		Odone[0] = 1
		return
	
	if( Owait[0] == 1 ):
		if( Oloc[0] == Otarget[0] ):
			Owait[0] = 1
			Onext[0] = 2
		else:
			Onext[0] = 0
		return
		
	if( Olock[0] == 0 ):
		for i in range( Oindex[0], len(queue) ):
			if i == ( len(queue) -1 ):
				Odone[0] = 1
				break
			if queue[i] == 'O' :
				Otarget[0] = int(queue[i+1])
				Oindex[0] = i + 1
				Olock[0] = 1
				break
				
	if ( Otarget[0]<0 ):
			Odone[0] = 1
			return
			
	if( Oloc[0] == Otarget[0] ):
		Owait[0] = 1
		Onext[0] = 2
		return
		
	if( Oloc[0] < Otarget[0] ):
		Owait[0] = 0
		Onext[0] = 1
		return
	else:
		Owait[0] = 0
		Onext[0] = -1
		return


def B_perform_action():
	if(Bdone[0]==1):
		return

	if (Bnext[0] == 2 and turn[0]=='B' ):
		Bwait[0] = 0
		pressed[0] = 1
		num_buttons[0] = num_buttons[0] - 1
		Block[0] = 0
		if( num_buttons[0] == 0 ):
			Bdone[0] = 1
		return

	elif( Bnext[0] == 0 ):
		Bwait[0] = 1
		return
	
	if (Bnext[0] == -1 ):
		Bloc[0] = Bloc[0] - 1
		return

	elif(Bnext[0] == 1 ):
		Bloc[0] = Bloc[0] + 1
		return
	
	return


def O_perform_action():
	if(Odone[0]==1):
		return

	if (Onext[0] == 2 and turn[0]=='O' ):
		Owait[0] = 0
		pressed[0] = 1 
		num_buttons[0] = num_buttons[0] - 1
		Olock[0] = 0
		if( num_buttons[0] == 0 ):
			Odone[0] = 1
		return

	elif( Onext[0] == 0 ):
		Owait[0] = 1
		return
	
	if (Onext[0] == -1 ):
		Oloc[0] = Oloc[0] - 1
		return

	elif(Onext[0] == 1 ):
		Oloc[0] = Oloc[0] + 1
		return

	return


def clear_pressed():
	pressed[0] = 0
	return
	
def switch_turns():
	for i in range (turnIndex[0],len(queue)):
		if( queue[i] == 'B' ):
			turn[0] = 'B'
			turnIndex[0] = i + 1 
			break
		elif( queue[i] == 'O' ):
			turn[0] = 'O'
			turnIndex[0] = i + 1
			break
	#print "turn: " + str(turn[0])
	return


for i in range(0,len(lines)):
	num_buttons[0] = int((lines[i].split())[0] )
	queue =  str(" ".join((lines[i].split())[1:])).split() 
	turn[0] = queue[0]
	turnIndex[0] = 1
	while(True):
		B_calculate_next_action()
		O_calculate_next_action()
		B_perform_action()
		O_perform_action()

		if ( pressed[0] == 1 ):
			clear_pressed()
			switch_turns()
			if( Bdone[0]==1 and Odone[0]==1 ):
				break

		time = time + 1
	print "Case #"+str(i+1)+": "+str(time)
	time = 0
	pressed[0] = 0
	Bdone[0] = 0
	Odone[0] = 0
	Bwait[0] = 0
	Owait[0] = 0
	Btarget[0] = -1
	Otarget[0] = -1
	Bnext[0] = 0
	Onext[0] = 0
	Bloc[0]  = 0
	Oloc[0]  = 0
	Block[0] = 0
	Olock[0] = 0
	Bindex[0] = 0
	Oindex[0] = 0
			
			