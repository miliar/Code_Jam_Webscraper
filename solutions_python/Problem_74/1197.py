
def total_time(sequence):
	pos = {'B':1,'O':1}
	other_color = {'B':'O','O':'B'}
	done = {'B':False,'O':False}
	total = 0
	next_other = None
	for i,button in enumerate(sequence):
		color,button_pos = button
		other = other_color[color]
		#handle current bot

		#move to next button, and push it
		elapsed = abs(pos[color]-button_pos)+1
		pos[color] = button_pos
		total += elapsed
		
		#find next_bot's location
		if next_other==None and not done[other]:
			#find next for other bot
			for next in sequence[i:]:
				ncolor,npos = next
				if ncolor == other:
					next_other = next
					break
		#can still be None
		if next_other == None: #all done
			done[other] = True
			continue
		#how far can we go in elapsed?
		ncolor,npos = next_other
		if elapsed >= abs(pos[other]-npos): #all the way
			pos[other] = npos #also works if we're there
		else: #get elasped units closer
			if pos[other] < npos: 
				pos[other] += elapsed
			if pos[other] > npos:
				pos[other] -= elapsed
		next_other = None
	return total

def parse_file(filename):
	result = []
	file = open(filename)
	file.readline()
	for line in file:
		line_vals = line.split(" ")
		colors = line_vals[1::2]
		pos = map(int,line_vals[2::2])
		sequence = zip(colors,pos)
		result.append(sequence)
	return result

for i,sequence in enumerate(parse_file("A-small-attempt1.in")):
	print "Case #"+str(i+1)+":",total_time(sequence)
