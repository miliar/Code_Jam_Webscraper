# Bot Trust
# Google Code Jam
# Ameer Ayoub <ameer.ayoub@gmail.com>
# 9:57pm 5/6/2011

def getOtherBot(bot):
	if bot == 'O' or bot == 'o':
		return 'B'
	else:
		return 'O'
		
def print_positions(b_p, o_p):
	print "Orange Position:", o_p, "; Blue Position: ", b_p
	
def print_targets(b_t, o_t):
	print "Orange Target:", o_t, "; Blue Target: ", b_t

def getNextMove(seq, bot, ind):
	# Return the next available move for a robot based
	# on the current move
	other_bot = getOtherBot(bot)
	move_counter = 0
	for m in range(len(seq)):
		if seq[m][0] == bot:
			if(move_counter == ind):
				if m > 0 and seq[m-1][0] == other_bot:
					return (seq[m-1][1], seq[m][1], m)
				else:
					return (-1, seq[m][1], m)
			else:
				move_counter += 1
	return (-1, -1, len(seq))

def BotSimulation(seq):
	print_debug = False
	time = 0
	b_i = 0
	o_i = 0
	b_position = 1
	o_position = 1
	blue_ready = False
	orange_ready = False
	blue_ready_flag = False
	orange_ready_flag = False
	b_target = getNextMove(seq, 'B', b_i)
	o_target = getNextMove(seq, 'O', b_i)
	
	while(b_target[1] != -1 or o_target[1] != -1):
		time += 1
		if(b_position == b_target[1]):
			# Cool we are in position to push blue
			if(b_target[0] == -1 or blue_ready):
				# Cool we can push blue so
				blue_ready = False
				b_i += 1
				if(o_target[0] == b_position and b_target[2] == o_target[2]-1):
					orange_ready_flag = True
		elif(b_position < b_target[1]):
			b_position += 1
		elif(b_target[1] != -1):
			b_position -= 1
		if(o_position == o_target[1]):
			# Cool we are in position to push orange
			if(o_target[0] == -1 or orange_ready):
				# Cool we can push orange so
				orange_ready = False
				o_i += 1
				if(b_target[0] == o_position and o_target[2] == b_target[2]-1):
					blue_ready_flag = True
		elif(o_position < o_target[1]):
			o_position += 1
		elif(o_target[1] != -1):
			o_position -= 1
		if(blue_ready_flag):
			blue_ready = True
			blue_ready_flag = False
		if(orange_ready_flag):
			orange_ready = True
			orange_ready_flag = False
		if print_debug:
			print_positions(b_position, o_position)
			print_targets(b_target, o_target)
			print "Orange Ready?", orange_ready
			print "Blue Ready?", blue_ready
		b_target = getNextMove(seq, 'B', b_i)
		o_target = getNextMove(seq, 'O', o_i)
	return time
	
def MoveTest():
	test_sequence = [('B', 1), ('O', 1), ('O', 1), ('O', 1), ('B', 1), ('B', 1), ('O', 1), ('O', 1), ('B', 1), ('B', 1)]
	for i in range(len(test_sequence)):
		print "Blue Move:", getNextMove(test_sequence, 'B', i)
		print "Orange Move:", getNextMove(test_sequence, 'O', i)
		print "\n"
	
def SimulateTest():
	test_sequence1 = [('B', 1), ('O', 1), ('O', 1), ('O', 1), ('B', 1), ('B', 1), ('O', 2)]#, ('O', 1), ('B', 1), ('B', 1)]	
	#B 1 O 1 O 1 O 1 B 1 B 1 O 1 O 1 B 1 B 1
	print "Time Required: \n", BotSimulation(test_sequence1)
	#test_sequence2 = [('O', 5), ('O', 8), ('B', 100)]
	#print "Time Required: \n", BotSimulation(test_sequence2)
	#test_sequence3 = [('B', 2), ('B', 1)]
	#print "Time Required: \n", BotSimulation(test_sequence3)
	
def executeMain():
	f = open("bot.in")
	o = open("bot.out", "w")
	num_cases = 0
	i = 0
	line = f.readline()
	if(line):
		num_cases = int(line)
	while(i < num_cases):
		line = f.readline()
		this_seq = []
		split_line = line.split(' ')
		num_seq = int(split_line[0])
		j = 0
		while(j < num_seq):
			this_seq.append((split_line[j*2 + 1], int(split_line[j*2 + 2])))
			j += 1
		o.write("Case #"+str(i+1)+": "+str(BotSimulation(this_seq))+"\n")
		i += 1

if __name__ == "__main__":
	#MoveTest()
	#SimulateTest()
	executeMain()
